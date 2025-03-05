import os
import requests
import json
from openai import OpenAI
from dotenv import load_dotenv

from constants import FLIGHT_STATUS_SYSTEM_PROMPT_LOCAL, USER_FLIGHT_REQUEST_PROMPT_LOCAL, ASSISTANT_SYSTEM_PROMPT_LOCAL, ASSISTANT_PROMPT_LOCAL

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
base_url = os.getenv('OPENAI_BASE_URL')
client = OpenAI(base_url=base_url, api_key=api_key)

def flight_details(flight_request_prompt):
    """
    This function is used to get the flight details for a flight from the flight request prompt which is a natural language request string.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": FLIGHT_STATUS_SYSTEM_PROMPT_LOCAL},
            {"role": "user", "content": USER_FLIGHT_REQUEST_PROMPT_LOCAL.format(flight_request_prompt=flight_request_prompt)}
        ]    
    )
    url = response.choices[0].message.content.replace("```", "").replace("plaintext", "").replace("url", "").replace("\n", "").strip()

    print(f"Assistant: Making request with url: {url}")

    access_key = os.getenv('FLIGHTS_API_ACCESS_TOKEN')
    url = url.format(access_key=access_key)
    response = requests.get(url)

    return response.json()



tools_dict = {
    "flight_details": flight_details
}

tools = [{
    "type": "function",
    "function": {
        "name": "flight_details",
        "description": "Get the flight details for a flight from the flight request prompt which is a natural language request string.",
        "parameters": {
            "type": "object",
            "properties": {
                "flight_request_prompt": {
                    "type": "string",
                    "description": "The flight request prompt which is a natural language request string. Behave like a travel agent and ask for the details of the flight."
                }
            },
            "required": ["flight_request_prompt"]
        }
    }
}]

original_messages = [ {"role": "system", "content": ASSISTANT_SYSTEM_PROMPT_LOCAL}]
while True:
    user_message = input("User: ")
    original_messages.append({"role": "user", "content": user_message})
    import pdb; pdb.set_trace()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=original_messages,
        tools=tools
    )

    tool_calls = response.choices[0].message.tool_calls
    while tool_calls is not None and len(tool_calls) > 0:
        failed_tool_call = False
        failure_message = ""
        tool_responses = []
        for tool_call in tool_calls:
            tool_function = tools_dict.get(tool_call.function.name, None)
            if not tool_function:
                failed_tool_call = True
                failure_message = f"The tool {tool_call.function.name} is not available. Please try again with a different tool available tools are {tools_dict.keys()}."
                break
            try:
                tool_response = tool_function(**json.loads(tool_call.function.arguments))
                tool_responses.append(tool_response)
            except Exception as e:
                failed_tool_call = True
                failure_message = f"The tool {tool_call.function.name} failed with exception {e}"

        if failed_tool_call:
            messages = original_messages + [
                {"role": "assistant", "content": failure_message},
            ]
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                tools=tools
            )
            tool_calls = response.choices[0].message.tool_calls
            continue
        
        messages = original_messages + [
            {"role": "assistant", "content": ASSISTANT_PROMPT_LOCAL.format(tool_call_responses=json.dumps(tool_responses))}
        ]
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=tools
        )
        tool_calls = response.choices[0].message.tool_calls
        if tool_calls is None or len(tool_calls) == 0:
            break
    
    print(f"Assistant: {response.choices[0].message.content}")
    original_messages.append({"role": "assistant", "content": response.choices[0].message.content})

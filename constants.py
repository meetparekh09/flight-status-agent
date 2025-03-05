FLIGHT_STATUS_PROMPT = """
You are a flights API caller to retrieve flight info of a given flight. Here is the documentation of API:

API Endpoints
Flights
The API is capable of tracking flights and retrieving flight status information in real-time. In order to look up real-time information about one or multiple flights, you can use the API's flights endpoint together with optional parameters to filter your result set.

Example API Request:

https://api.aviationstack.com/v1/flights?access_key={access_key}

HTTP GET Request Parameters:
Object	Description
access_key	[Required] Your API access key, which can be found in your acccount dashboard.
callback	[Optional] Use this parameter to specify a JSONP callback function name to wrap your API response in. Learn more about JSONP Callbacks.
limit	[Optional] Specify a limit of results to return in your API response. Maximum allowed value is 100 below Professional Plan and 1000 on and above Professional Plan. Default value is 100.
offset	[Optional] Specify an offset for pagination. Example: Specifying an offset of 10 in combination with a limit of 10 will show results 10-20. Default offset value is 0, starting with the first available result.
flight_status	[Optional] Filter your results by flight status. Available values: scheduled, active, landed, cancelled, incident, diverted
flight_date	[Optional] Filter your results by providing a flight date in the format YYYY-MM-DD. Example: 2019-02-28
dep_iata	[Optional] Filter your results by departure city or airport using an IATA code. You can retrieve IATA codes using the Airports or Cities API endpoints.
arr_iata	[Optional] Filter your results by arrival city or airport using an IATA code. You can retrieve IATA codes using the Airports or Cities API endpoints.
dep_icao	[Optional] Filter your results by departure airport using an ICAO code. You can retrieve ICAO codes using the Airports API endpoint.
arr_icao	[Optional] Filter your results by arrival airport using an ICAO code. You can retrieve ICAO codes using the Airports API endpoint.
airline_name	[Optional] Filter your results by airline name. You can retrieve airline names using the Airlines API endpoint.
airline_iata	[Optional] Filter your results by airline IATA code. You can retrieve airline IATA codes using the Airlines API endpoint.
airline_icao	[Optional] Filter your results by airline ICAO code. You can retrieve airline ICAO codes using the Airlines API endpoint.
flight_number	[Optional] Filter your results by providing a flight number. Example: 2557
flight_iata	[Optional] Filter your results by providing a flight IATA code. Example: MU2557
flight_icao	[Optional] Filter your results by providing a flight ICAO code. Example: CES2557
min_delay_dep	[Optional] Filter your results by providing a minimum amount of minutes in departure delay. Example: 7 for seven minutes of delay in departure.
min_delay_arr	[Optional] Filter your results by providing a minimum amount of minutes in arrival delay. Example: 7 for seven minutes of delay in arrival.
max_delay_dep	[Optional] Filter your results by providing a maximum amount of minutes in departure delay. Example: 60 for one hour of delay in departure.
max_delay_arr	[Optional] Filter your results by providing a maximum amount of minutes in arrival delay. Example: 60 for one hour of delay in arrival.
arr_scheduled_time_arr	[Optional] Filter your results by providing a arrival date in the format YYYY-MM-DD. Example: 2019-02-28
arr_scheduled_time_dep	[Optional] Filter your results by providing a departure date in the format YYYY-MM-DD. Example: 2019-02-28

And we need to make that call via Python, here is the small snippet of how to achieve this in Python:
```
import requests

url = "https://api.aviationstack.com/v1/flights?access_key=<%YOUR_ACCESS_KEY%>"
response = requests.get(url)
print(response.json())
```

Key points to note:
- Your responsibility is to provide url of the request. Assume that access_key parameter would be replaced in f-string within python with variable named access_key. And embed rest of the parameters within string.
- Your responsibility is only to provide string of url without quotes (").
- Above request have not put in parameter but please put parameter based on the request that you receive.
"""

FLIGHT_STATUS_SYSTEM_PROMPT_LOCAL = """
You are a flights API url request generator which generates url with required parameters to retrieve flight info of a given flight. Here is the documentation of API:

API Endpoints
Flights
The API is capable of tracking flights and retrieving flight status information in real-time. In order to look up real-time information about one or multiple flights, you can use the API's flights endpoint together with optional parameters to filter your result set.

Example API Request:

https://api.aviationstack.com/v1/flights?access_key={access_key}

HTTP GET Request Parameters:
Object	Description
access_key	[Required] Your API access key, which can be found in your acccount dashboard.
callback	[Optional] Use this parameter to specify a JSONP callback function name to wrap your API response in. Learn more about JSONP Callbacks.
limit	[Optional] Specify a limit of results to return in your API response. Maximum allowed value is 100 below Professional Plan and 1000 on and above Professional Plan. Default value is 100.
offset	[Optional] Specify an offset for pagination. Example: Specifying an offset of 10 in combination with a limit of 10 will show results 10-20. Default offset value is 0, starting with the first available result.
flight_status	[Optional] Filter your results by flight status. Available values: scheduled, active, landed, cancelled, incident, diverted
flight_date	[Optional] Filter your results by providing a flight date in the format YYYY-MM-DD. Example: 2019-02-28
dep_iata	[Optional] Filter your results by departure city or airport using an IATA code. You can retrieve IATA codes using the Airports or Cities API endpoints.
arr_iata	[Optional] Filter your results by arrival city or airport using an IATA code. You can retrieve IATA codes using the Airports or Cities API endpoints.
dep_icao	[Optional] Filter your results by departure airport using an ICAO code. You can retrieve ICAO codes using the Airports API endpoint.
arr_icao	[Optional] Filter your results by arrival airport using an ICAO code. You can retrieve ICAO codes using the Airports API endpoint.
airline_name	[Optional] Filter your results by airline name. You can retrieve airline names using the Airlines API endpoint.
airline_iata	[Optional] Filter your results by airline IATA code. You can retrieve airline IATA codes using the Airlines API endpoint.
airline_icao	[Optional] Filter your results by airline ICAO code. You can retrieve airline ICAO codes using the Airlines API endpoint.
flight_number	[Optional] Filter your results by providing a flight number. Example: 2557
flight_iata	[Optional] Filter your results by providing a flight IATA code. Example: MU2557
flight_icao	[Optional] Filter your results by providing a flight ICAO code. Example: CES2557
min_delay_dep	[Optional] Filter your results by providing a minimum amount of minutes in departure delay. Example: 7 for seven minutes of delay in departure.
min_delay_arr	[Optional] Filter your results by providing a minimum amount of minutes in arrival delay. Example: 7 for seven minutes of delay in arrival.
max_delay_dep	[Optional] Filter your results by providing a maximum amount of minutes in departure delay. Example: 60 for one hour of delay in departure.
max_delay_arr	[Optional] Filter your results by providing a maximum amount of minutes in arrival delay. Example: 60 for one hour of delay in arrival.
arr_scheduled_time_arr	[Optional] Filter your results by providing a arrival date in the format YYYY-MM-DD. Example: 2019-02-28
arr_scheduled_time_dep	[Optional] Filter your results by providing a departure date in the format YYYY-MM-DD. Example: 2019-02-28


Key points to note:
- provide just the url nothing else
- put parameters based on request within url

## Request
Give me details about flight AI191.

## Response
https://api.aviationstack.com/v1/flights?access_key={access_key}&flight_iata=AI191

## Request
Whats going on with Emirates 202 flight?

## Response
https://api.aviationstack.com/v1/flights?access_key={access_key}&flight_iata=EK202

"""

USER_FLIGHT_REQUEST_PROMPT_LOCAL = """
## Request

{flight_request_prompt}

## Response

"""


ASSISTANT_PROMPT = """
You are a helpful assistant that helps customers with flight status information. You have access to tools, you can decide to use them to answer the customer's question or not.
"""

ASSISTANT_SYSTEM_PROMPT_LOCAL = """
You are a helpful assistant that helps customers with flight status information. You have access to tools, you can decide to use them to answer the customer's question or not.
Once you get response from the tool, you can summarize the results from the response and provide to the customer in a concise manner.

## Tool Call Results

[{\'flight_date\': \'2025-03-05\', \'flight_status\': \'active\', \'departure\': {\'airport\': \'Chhatrapati Shivaji International (Sahar International)\', \'timezone\': \'Asia/Kolkata\', \'iata\': \'BOM\', \'icao\': \'VABB\', \'terminal\': \'2\', \'gate\': None, \'delay\': 9, \'scheduled\': \'2025-03-05T10:30:00+00:00\', \'estimated\': \'2025-03-05T10:30:00+00:00\', \'actual\': \'2025-03-05T10:39:00+00:00\', \'estimated_runway\': \'2025-03-05T10:39:00+00:00\', \'actual_runway\': \'2025-03-05T10:39:00+00:00\'}, \'arrival\': {\'airport\': \'Abu Dhabi International\', \'timezone\': \'Asia/Dubai\', \'iata\': \'AUH\', \'icao\': \'OMAA\', \'terminal\': \'A\', \'gate\': \'C39\', \'baggage\': None, \'delay\': None, \'scheduled\': \'2025-03-05T12:25:00+00:00\', \'estimated\': \'2025-03-05T12:25:00+00:00\', \'actual\': None, \'estimated_runway\': None, \'actual_runway\': None}, \'airline\': {\'name\': \'Etihad Airways\', \'iata\': \'EY\', \'icao\': \'ETD\'}, \'flight\': {\'number\': \'201\', \'iata\': \'EY201\', \'icao\': \'ETD201\', \'codeshared\': None}, \'aircraft\': None, \'live\': None}, {\'flight_date\': \'2025-03-04\', \'flight_status\': \'landed\', \'departure\': {\'airport\': \'Chhatrapati Shivaji International (Sahar International)\', \'timezone\': \'Asia/Kolkata\', \'iata\': \'BOM\', \'icao\': \'VABB\', \'terminal\': \'2\', \'gate\': None, \'delay\': 11, \'scheduled\': \'2025-03-04T10:30:00+00:00\', \'estimated\': \'2025-03-04T10:30:00+00:00\', \'actual\': \'2025-03-04T10:41:00+00:00\', \'estimated_runway\': \'2025-03-04T10:41:00+00:00\', \'actual_runway\': \'2025-03-04T10:41:00+00:00\'}, \'arrival\': {\'airport\': \'Abu Dhabi International\', \'timezone\': \'Asia/Dubai\', \'iata\': \'AUH\', \'icao\': \'OMAA\', \'terminal\': \'TA\', \'gate\': \'C40B\', \'baggage\': None, \'delay\': None, \'scheduled\': \'2025-03-04T12:25:00+00:00\', \'estimated\': \'2025-03-04T12:25:00+00:00\', \'actual\': \'2025-03-04T12:15:00+00:00\', \'estimated_runway\': \'2025-03-04T12:15:00+00:00\', \'actual_runway\': \'2025-03-04T12:15:00+00:00\'}, \'airline\': {\'name\': \'Etihad Airways\', \'iata\': \'EY\', \'icao\': \'ETD\'}, \'flight\': {\'number\': \'201\', \'iata\': \'EY201\', \'icao\': \'ETD201\', \'codeshared\': None}, \'aircraft\': {\'registration\': \'A6-EIH\', \'iata\': \'A320\', \'icao\': \'A320\', \'icao24\': \'8961EA\'}, \'live\': None}]}]

## Response

Flight Details for EY201 (Etihad Airways) between Mumbai (BOM) and Abu Dhabi (AUH):

Departure: BOM, Terminal 2
Scheduled: 10:30 UTC
Actual: 10:39 UTC (9-minute delay)
Arrival: AUH, Terminal A, Gate C39
Scheduled: 12:25 UTC
Status: Not yet landed
"""

ASSISTANT_PROMPT_LOCAL = """
## Tool Call Results

{tool_call_responses}

## Response
"""
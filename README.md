# Flight Status AI Agent

This is an AI-powered flight status assistant that helps users get flight information using natural language queries. The agent leverages OpenAI's GPT-4 model and the Aviation Stack API to provide real-time flight information through a conversational interface.

## Features

- Natural language processing for flight queries
- Real-time flight status information via Aviation Stack API
- Interactive command-line interface
- OpenAI function calling for structured data extraction
- Error handling and retry mechanisms

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Aviation Stack API access token

## Environment Variables Required

- `OPEN_AI_API_KEY`: Your OpenAI API key
- `FLIGHTS_API_ACCESS_TOKEN`: Your Aviation Stack API access token

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
   - Create a `.env` file in the root directory
   - Add your API keys:
     ```
     OPEN_AI_API_KEY=your_openai_api_key_here
     FLIGHTS_API_ACCESS_TOKEN=your_aviation_stack_token_here
     ```

## Usage

Run the flight status agent:
```bash
python flights.py
```

Example queries you can try:
- "What's the status of flight AA123?"
- "Show me flights from JFK to LAX today"
- "Is there any delay in United Airlines flight UA456?"

## How It Works

1. The agent uses GPT-4 to understand natural language queries about flights
2. It converts these queries into structured API calls to Aviation Stack
3. The flight data is fetched and processed
4. GPT-4 then formats the response in a user-friendly way

## OpenAI Tools Implementation

The project demonstrates OpenAI's function calling feature through:
- A custom `flight_details` function that processes natural language queries
- System prompts that guide the AI in interpreting flight requests
- Tool definitions that specify the expected input parameters

## Project Structure

```
├── README.md
├── requirements.txt
├── flights.py        # Main application file
├── constants.py      # System prompts and API documentation
└── .env             # Environment variables (create this file)
```

## API Integration

The project uses the Aviation Stack API which provides:
- Real-time flight tracking
- Comprehensive flight status information
- Support for various query parameters (flight number, airport codes, dates, etc.)

## Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
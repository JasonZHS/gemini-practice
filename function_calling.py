from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()

# Define a function that the model can call (to access external information)
def get_current_weather(city: str) -> str:
    """Returns the current weather in a given city. For this example, it's hardcoded."""
    if 'boston' in city.lower():
        return 'The weather in Boston is 15°C and sunny.'
    else:
        return f'Weather data for {city} is not available.'

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents='Use the tool you have to answer this question: What is the weather in SF?',
    config=types.GenerateContentConfig(
        tools=[get_current_weather] # Make the function available to the model as a tool
    ),
)

# The model may respond with a request to call the function
if response.function_calls:
    print('Function calls requested by the model:')
    for function_call in response.function_calls:
        print(f'- Function: {function_call.name}')
        print(f'- Args: {dict(function_call.args)}')
else:
    print('The model responded directly:')
    print(response.text)
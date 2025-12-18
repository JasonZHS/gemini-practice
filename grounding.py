from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents='What was the score of the latest Olympique Lyonais game?',
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(google_search=types.GoogleSearch())
        ]
    ),
)

print(response.text)
# Search details
print(f'Search Query: {response.candidates[0].grounding_metadata.web_search_queries}')
# Inspect grounding metadata
print(response.candidates[0].grounding_metadata.search_entry_point.rendered_content)
# Urls used for grounding
print(f"Search Pages: {', '.join([site.web.title for site in response.candidates[0].grounding_metadata.grounding_chunks])}")
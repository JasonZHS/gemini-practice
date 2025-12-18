import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file")

genai.configure(api_key=api_key)

def main():
    try:
        # Use the gemini-1.5-flash model
        model = genai.GenerativeModel("models/gemini-2.0-flash")
        
        # Send a simple prompt
        response = model.generate_content("Hello! What is your name and what can you do?")
        
        print("Response from Gemini:")
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

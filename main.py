import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables.")
        return

    # Configure the Gemini API
    genai.configure(api_key=api_key)

    # List available models
    print("Available models:")
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")

    # Initialize the model
    model_name = 'gemini-2.0-flash'
    print(f"\nUsing model: {model_name}")
    model = genai.GenerativeModel(model_name)

    prompt = "Write a short poem about coding."
    
    print(f"Prompt: {prompt}")
    print("-" * 20)

    try:
        response = model.generate_content(prompt)
        print(response.text)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

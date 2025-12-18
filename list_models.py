import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def main():
    print("Listing available models:")
    try:
        for m in genai.list_models():
            print(f"Name: {m.name}, Display Name: {m.display_name}, Methods: {m.supported_generation_methods}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

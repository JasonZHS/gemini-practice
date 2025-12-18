from google import genai
from PIL import Image
from io import BytesIO
from dotenv import load_dotenv
load_dotenv()

client = genai.Client()

prompt = """
Create a picture of my cat eating a nano-banana in a fancy restaurant under the gemini constellation
"""
image = Image.open('generated_image.png')

# Create the chat
chat = client.chats.create(model='gemini-2.5-flash-image')
# Send the image and ask for it to be edited
response = chat.send_message([prompt, image])

# Get the text and the image generated
for i, part in enumerate(response.candidates[0].content.parts):
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save(f'generated_image_{i}.png') # Multiple images can be generated

# Continue iterating
chat.send_message('Can you make it a bananas foster?')
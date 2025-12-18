import time
from google import genai
from google.genai import types
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

client = genai.Client()

# Video generation is an async operation
operation = client.models.generate_videos(
    model='veo-3.0-fast-generate-001',
    prompt='Panning wide shot of a calico kitten sleeping in the sunshine',
    config=types.GenerateVideosConfig(
        aspect_ratio='16:9',  # '16:9' or '9:16'
        number_of_videos=1, # supported value is 1-4, use 1 by default
        duration_seconds=8, # supported value is 5-8
    ),
)

# Poll for completion
while not operation.done:
    time.sleep(20)
    operation = client.operations.get(operation)

for n, generated_video in enumerate(operation.response.generated_videos):
    client.files.download(file=generated_video.video) # just file=, no need for path= as it doesn't save yet
    generated_video.video.save(f'video{n}.mp4')  # saves the video
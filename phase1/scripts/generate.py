import openai
import requests
import os
from PIL import Image
from io import BytesIO

# OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to generate an image with DALLE and save it locally
def generate_image(prompt, output_path):
    # Ensure the prompt is within the 1000 character limit
    if len(prompt) > 1000:
        prompt = prompt[:1000]
    
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"  # Image resolution size
    )
    
    # Extract the URL of the generated image
    image_url = response['data'][0]['url']
    #print(f"Generated image URL: {image_url}")

    # Download and save the image locally
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))
    image.save(output_path)  # Save image to the provided output path
    print(f"Image saved to {output_path}")
    return output_path

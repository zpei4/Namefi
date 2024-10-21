from pathlib import Path
from detect import detect_billboard
from overlay import overlay_text_on_billboard
from generate import generate_image

script_directory = Path(__file__).parent

def main():
    # Generate the image
    prompt = "A large billboard on the side of a busy highway with cars passing by. The billboard is blank, ready for an advertisement, and is surrounded by trees and open sky. The lighting is bright and sunny, creating a realistic outdoor environment."

    output_directory = script_directory.parent / 'data'

    # Create the data directory if it does not exist
    output_directory.mkdir(exist_ok=True)

    # Define the output path for the generated image
    output_image_path = output_directory / 'generated_image.jpg'
    generated_image_path = generate_image(prompt, output_image_path)

    # Detect billboard in the generated image
    billboard_coordinates = detect_billboard(generated_image_path)

    if not billboard_coordinates:
        print("No billboard detected.")
        return

    # Get user input for text overlay
    user_text = input("Enter the text to overlay on the billboard: ")

    # Overlay text on the detected billboard
    output_directory = script_directory.parent / 'output'
    output_directory.mkdir(exist_ok=True)
    output_image_path = output_directory/ 'output_image.jpg'
    overlay_text_on_billboard(generated_image_path, output_image_path, user_text, billboard_coordinates)

if __name__ == "__main__":
    main()
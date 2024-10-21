from PIL import Image, ImageDraw, ImageFont

def overlay_text_on_billboard(image_path, output_path, text, billboards):
    # Check if the text is a list; if not, apply the same text to all billboards
    if isinstance(text, str):
        text = [text] * len(billboards)  # Repeat the same text for each billboard if only one text provided

    # Open the image once for editing
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    
    # Set up the font (you can specify a .ttf file, or leave it as default)
    font_size = 50
    font_color = (50, 168, 119)  # Namefi green
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    # Iterate over each detected billboard and add the corresponding text
    for i, (x, y, width, height) in enumerate(billboards):
        # Calculate the center of the billboard
        center_x = x + width // 2
        center_y = y + height // 2

        # Calculate the size of the text to adjust the position
        text_box = draw.textbbox((0, 0), text[i], font=font)
        text_width = text_box[2] - text_box[0]
        text_height = text_box[3] - text_box[1]

        # Adjust the position so the center of the text is aligned with the center of the billboard
        adjusted_position = (center_x - text_width // 2, center_y - text_height // 2)

        # Add text to the image at the adjusted position
        draw.text(adjusted_position, text[i], font=font, fill=font_color)

    # Save the edited image
    image.save(output_path)
    print(f"Text added to all billboards and image saved as {output_path}")
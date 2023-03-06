from PIL import Image

def crop_image(input_path, output_path, crop_width, crop_height):
    # Open the input image file
    with Image.open(input_path) as image:
        # Get the width and height of the input image
        width, height = image.size

        # Calculate the center of the image
        center_x = width // 2
        center_y = height // 2

        # Calculate the coordinates for the top-left corner of the crop
        left = center_x - crop_width // 2
        top = center_y - crop_height // 2

        # Calculate the coordinates for the bottom-right corner of the crop
        right = left + crop_width
        bottom = top + crop_height

        # Crop the image
        cropped_image = image.crop((left, top, right, bottom))

        # Save the cropped image to the output file
        cropped_image.save(output_path)

# Example usage:
crop_image("input.jpg", "output.jpg", 800, 600)

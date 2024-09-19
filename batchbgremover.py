import argparse
from rembg import remove
from PIL import Image

# Function to remove the background
def remove_background(input_image_path, output_image_path):
    input_image = Image.open(input_image_path)
    output_image = remove(input_image)
    output_image.save(output_image_path)
    print(f"Background removed: {output_image_path}")

# Function to change background color
def change_background_color(input_image_path, output_image_path, bg_color):
    input_image = Image.open(input_image_path).convert("RGBA")
    
    # Create a new image with the desired background color
    background = Image.new("RGBA", input_image.size, bg_color)
    
    # Paste the input image on top of the background
    background.paste(input_image, (0, 0), input_image)
    
    # Convert to RGB and save the result
    background.convert("RGB").save(output_image_path)
    print(f"Background color changed to {bg_color}: {output_image_path}")

# Main function to handle command line arguments
def main():
    parser = argparse.ArgumentParser(description="Remove or change image background.")
    
    parser.add_argument('input', type=str, help="Path to the input image file.")
    parser.add_argument('output', type=str, help="Path to save the output image file.")
    parser.add_argument('--bg-color', type=int, nargs=3, metavar=('R', 'G', 'B'), help="Optional background color in RGB format (e.g., --bg-color 255 0 0 for red).")
    
    args = parser.parse_args()
    
    # Remove background
    if args.bg_color:
        change_background_color(args.input, args.output, tuple(args.bg_color))
    else:
        remove_background(args.input, args.output)

if __name__ == "__main__":
    main()

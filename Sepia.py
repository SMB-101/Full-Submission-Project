from KnochSnowflake import Image

def apply_sepia(image_path, output_path):
    image = Image.open(image_path)
    pixels = image.load()
    
    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))
            
            # Apply sepia tone transformation
            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)
            
            # Ensure RGB values are within 0-255
            pixels[x, y] = (min(tr, 255), min(tg, 255), min(tb, 255))
    
    image.save(output_path)
    image.show()

# Example usage
apply_sepia("input.jpg", "output_sepia.jpg")

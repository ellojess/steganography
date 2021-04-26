"""
[Day 7] Assignment: Steganography
    - Turn in on Gradescope (https://make.sc/bew2.3-gradescope)
    - Lesson Plan: https://make-school-courses.github.io/BEW-2.3-Web-Security/#/Lessons/Steganography

Deliverables:
    1. All TODOs in this file.
    2. Decoded sample image with secret text revealed
    3. Your own image encoded with hidden secret text!
"""
# TODO: Run `pip3 install Pillow` before running the code.
from PIL import Image


def decode_image(path_to_png):
    """
    decodes png by isolating red channel and decoding by pixels 
    creates new black and white image from least significant bits 
    """
    # Open the image using PIL:
    encoded_image = Image.open(path_to_png)

    # Separate the red channel from the rest of the image:
    red_channel = encoded_image.split()[0]

    # Create a new PIL image with the same size as the encoded image:
    decoded_image = Image.new("RGB", encoded_image.size)
    pixels = decoded_image.load()
    x_size, y_size = encoded_image.size

    for x in range(x_size):
        for y in range(y_size):
            # use bin to get binary representation
            # if pixel string ends with 0, then make pixel black
            if bin(red_channel.getpixel((x, y)))[-1] == '0':
                pixels[x, y] = (0, 0, 0)
            # else if pixel ends with 1, then make pixel white
            else:
                pixels[x, y] = (255, 255, 255)


    # DO NOT MODIFY. Save the decoded image to disk:
    decoded_image.save("decoded_image.png")

path_to_png = "doggo_encoded.png"
decode_image(path_to_png)


def encode_image(text_to_encode, image_to_encode):
    """
    Encode message into an image 
    """

    # Open the image using PIL:
    image_to_encode = Image.open(image_to_encode)

    # Split the different color channels
    red_channel = image_to_encode.split()[0]
    green_channel = image_to_encode.split()[1]
    blue_channel = image_to_encode.split()[2]

    # encode text into image 
    x_size, y_size = image_to_encode
    encoded_image = Image.new("RGB", (x_size, y_size))
    pixels = encoded_image.load()

    # text draw 
    image_text = write_text(text_to_encode, image_to_encode.s)
    black_white_encode = image_text.convert('1')

    for x in range(x_size):
        for y in range(y_size):
            red_channel_pix = bin(red_channel.getpixel(x, y))
            original_pix = red_channel_pix.getpixel((x, y))
            tencode_pix = bin(black_white_encode.getpixel(x, y))

            if tencode_pix[-1] == '1':
                red_channel_pix = red_channel_pix[:-1] + ''
            else :
                red_channel_pix = red_channel_pix[:-1] + ''
            
            pixels[x, y] = (int(red_channel_pix, 2), green_channel.getpixel(x, y), blue_channel.getpixel(x, y)) 
            
    encoded_image.save("encoded_image.png")




def write_text(text_to_write, image_size):
    """
    TODO: Add docstring and complete implementation.
    """
 
    image_text = Image.new("RGB", image_size)
    font = ImageFont.load_default().font
    drawer = ImageDraw.Draw(image_text)

    # Text wrapping. Change parameters for different text formatting
    margin = offset = 10

    for line in textwrap.wrap(text_to_write, width=60):
        drawer.text((margin,offset), line, font=font)
        offset += 10
    return image_text


if __name__ == '__main__':
    encode_image("hello world", "doggo_encoded.png")
    decode_image()
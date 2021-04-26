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

def encode_image(path_to_png):
    """
    TODO: Add docstring and complete implementation.
    """
    pass


def write_text(text_to_write):
    """
    TODO: Add docstring and complete implementation.
    """
    pass
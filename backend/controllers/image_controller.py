from typing import BinaryIO
from PIL import Image


def open_image(file: BinaryIO):
    try:
        Image.open(file)
        print("THIS WORKED")
    except Exception as e:
        print(e)

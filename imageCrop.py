from PIL import Image
import os
from pathlib import Path

def cropImage(imageAddress):
    print(imageAddress)
    # Open a image in RGB mode
    # In Windows, address should be raw text
    im = Image.open(imageAddress)

    # Setting the points for cropped image
    left = 0
    top = 207
    right = 450
    bottom = 848

    # Croped image of above dimension
    # It will not change original image
    im1 = im.crop((left, top, right, bottom))

    # Show the image in image viewer
    # imageOutputAddress = 'outputAddress'
    im1.save(imageAddress, quality=95)

# Traverse image files, crop file in turn
def cropFileInTurn(directory):
    # In windows, directory should be in raw text, r'C:\Users\xq127\Pictures\temp'
    for dirpath, dirnames, filenames in os.walk(directory):
        dir = Path(dirpath)
        for file in filenames:
            file = dir / file
            cropImage(file)

cropFileInTurn(r'C:\Users\xq127\Pictures\temp')
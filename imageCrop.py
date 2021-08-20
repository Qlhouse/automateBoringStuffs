from PIL import Image

def cropImage(imageAddress):
    # Open a image in RGB mode
    im = Image.open(r'imageAddress')

    # Size of the original image in pixels
    # This is not mandatory
    # width, height = im.size

    # Setting the points for cropped image
    left = 0
    top = 207
    right = 450
    bottom = 848

    # Croped image of above dimension
    # It will not change original image
    im1 = im.crop((left, top, right, bottom))

    # Show the image in image viewer
    imageOutputAddress = 'outputAddress'
    im1.save(r'imageOutputAddress', quality=95)


import cv2
import numpy as np

# Install openCV
'''
pip install opencv-python
'''

# Refer to websites
# [learnopencv.com](https://learnopencv.com/edge-detection-using-opencv/)
# [quora.com](https://www.quora.com/How-can-I-detect-an-object-from-static-image-and-crop-it-from-the-image-using-openCV)

#############  Output image information  ##############
def showImageInformation():
    image = cv2.imread(r'C:\Users\xq127\Desktop\Screenshot.jpg')
    print(image.shape)

def detectAngleAndRotateImage():
    pass

#############  Resize image  ################
def resizeDownImage():
    image = cv2.imread(r'C:\Users\xq127\Desktop\bookCrop.jpg')

    height, width, channels = image.shape

    # Scale down the image 0.6 times by specifying a single scale factor
    scaleDown = 1000 / width
    # scaleDown = 1000 / height
    resizeDown = cv2.resize(image, None, fx=scaleDown, fy=scaleDown, interpolation=cv2.INTER_AREA)

    cv2.namedWindow("Scale Down", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Scale Down", resizeDown)
    cv2.waitKey(0)

    return resizeDown

##### Crop Image #####
def cropImage():
    #  Crop images using OpenCV
    img = cv2.imread(r'C:\Users\xq127\Desktop\cropImage.png')

    # Print dimensions of the image
    print(img.shape)

    # Display the original image
    cv2.imshow("original", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Slicing to crop the image
    # cropped = img[start_row:end_row, start_col:end_col]
    croppedImage = img[180:280, 25:330]

    # Display the cropped image
    cv2.imshow("cropped", croppedImage)
    cv2.waitKey()
    cv2.destroyAllWindows()

##############  Image Threshold  #################


##############  Edge Detection  ##################
def sobelEdgeDetection():
    img = cv2.imread(r'C:\Users\xq127\Desktop\input_image-1.jpg', flags=0)

    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img, (3, 3), sigmaX=0, sigmaY=0)

    # Sobel edge detection
    # Sobel edge detection on the X axis
    sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F,
                       dx=1, dy=0, ksize=5)

    # Sobel edge detection on the Y axis
    sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F,
                       dx=0, dy=1, ksize=5)

    # Sobel edge detection conbined X and Y direction
    sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F,
                        dx=1, dy=1, ksize=5)

    # Display Sobel edge detection images
    cv2.imshow('Sobel X', sobelx)
    cv2.waitKey(0)

    cv2.imshow('Sobel Y', sobely)
    cv2.waitKey(0)

    cv2.imshow('Sobel X Y using Sobel() function', sobelxy)
    cv2.waitKey(0)

def cannyEdgeDetection():
    img = cv2.imread(r'C:\Users\xq127\Desktop\input_image-1.jpg', flags=0)

    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img, (3, 3), sigmaX=0, sigmaY=0)

    edges = cv2.Canny(image=img_blur, threshold1=20, threshold2=100)

    # Display Canny edge detection image
    cv2.imshow('Canny Edge Detection', edges)
    cv2.waitKey(0)


#############  Crop image after edge detected  ##############
def cropImageWithEdgeDetection():
    # Read the image
    # image = cv2.imread(r'C:\Users\xq127\Desktop\bookCrop.jpg')
    image = resizeDownImage()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Edge detection
    edged = cv2.Canny(gray, 2, 250)
    # cv2.namedWindow("Edged Image", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("Egded Image", edged)
    cv2.waitKey(0)

    # Find contours
    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, 
            cv2.CHAIN_APPROX_SIMPLE)

    # Crop image
    idx = 0
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        if w > 300 and h > 200:
            idx += 1
            newImage = image[y:y+h, x:x+w]
            cv2.imwrite(str(idx) + '.png', newImage)


# sobelEdgeDetection()
# cannyEdgeDetection()
cropImageWithEdgeDetection()
# showImageInformation()
# resizeDownImage()

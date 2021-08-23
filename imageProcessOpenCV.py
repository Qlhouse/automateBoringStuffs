import cv2

# Install openCV
'''
pip install opencv-python
'''

# Refer to websites
# [learnopencv.com](https://learnopencv.com/edge-detection-using-opencv/)
# [quora.com](https://www.quora.com/How-can-I-detect-an-object-from-static-image-and-crop-it-from-the-image-using-openCV)

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
    image = cv2.imread(r'C:\Users\xq127\Desktop\bookCrop.jpg')

    # Edge detection
    edged = cv2.Canny(image, 10, 100)
    cv2.imshow("Edged", edged)
    cv2.waitKey(0)

    # Apply closing function
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("Closed", closed)
    cv2.waitKey(0)

    # Find contours
    (cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, 
            cv2.CHAIN_APPROX_SIMPLE)

    for c in cnts:
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.02 * peri, True)
        cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)

    cv2.imshow("Output", image)
    cv2.waitKey(0)


# sobelEdgeDetection()
# cannyEdgeDetection()
cropImageWithEdgeDetection()

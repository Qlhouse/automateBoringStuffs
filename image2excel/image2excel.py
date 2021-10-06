import cv2
from matplotlib import image
import numpy as np
from numpy.core.numeric import outer
import pandas as pd
import matplotlib.pyplot as plt
import csv
from PIL import Image
import pytesseract
from conf import SOURCE_DIR, OUTPUT_DIR
import os


'''
# [Refer site](https://towardsdatascience.com/
# a-table-detection-cell-recognition-and-text-extraction-
# algorithm-to-convert-tables-to-excel-files-902edcf289ec)
'''


os.makedirs(SOURCE_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Read the image file
file = os.path.join(SOURCE_DIR, 'tableImg.jpg')
img = cv2.imread(file, 0)
# print(img.shape)


# Thresholding the image to a binary image
thresh, img_bin = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY | 
         cv2.THRESH_OTSU)

# Inverting the image
img_bin = 255-img_bin
invertedImg = os.path.join(OUTPUT_DIR, 'cv_inverted.png')
# cv2.imwrite(invertedImg, img_bin)

# Plotting the image to see the output
plotting = plt.imshow(img_bin, cmap='gray')
plt.show()


# Define a kernel to detect rectangular boxes, and the tabular structure
# Length (width) of kernel as 100th of total width
kernel_len = np.array(img).shape[1] // 100

# Define a vertical kernel to detect all vertical lines of image
ver_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, kernel_len))

# Defining a horizontal kernel to detect all horzontal lines of image
hor_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_len, 1))

# A kernel of 2x2
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))


# Use vertical kernal to detect and save the vertical lines in a jpg
image_1 = cv2.erode(img_bin, ver_kernel, iterations=3)
vertical_lines = cv2.dilate(image_1, ver_kernel, iterations=3)
verticalImg = os.path.join(OUTPUT_DIR, 'vertical.jpg')
# cv2.imwrite(verticalImg, vertical_lines)

# Plot the generated image
plotting = plt.imshow(image_1, cmap='gray')
plt.show()


# Use horizontal kernel to detect and save the horizontal lines in a jpg
image_2 = cv2.erode(img_bin, hor_kernel, iterations=3)
horizontal_lines = cv2.dilate(image_2, hor_kernel, iterations=3)
horizontalImg = os.path.join(OUTPUT_DIR, 'horizontal.jpg')
# cv2.imwrite(horizontalImg, horizontal_lines)

# Plot the generated image
plotting = plt.imshow(image_2, cmap='gray')
plt.show()


# Combine horizontal and vertical lines in a new third image, 
# with both having same weight
img_vh = cv2.addWeighted(vertical_lines, 0.5, horizontal_lines, 0.5, 0.0)

# Eroding and thresholding the image
img_vh = cv2.erode(~img_vh, kernel, iterations=2)
thresh, img_vh = cv2.threshold(img_vh, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
vhImg = os.path.join(OUTPUT_DIR, 'img_vh.jpg')
cv2.imwrite(vhImg, img_vh)

bitxor = cv2.bitwise_xor(img, img_vh)
bitnot = cv2.bitwise_not(bitxor)

# Plot the generated image
plotting = plt.imshow(bitnot, cmap='gray')
plt.show()


# Detect contours for following box detection
contours, hierarchy = cv2.findContours(img_vh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours from top to down
def sort_contours(cnts, method="left-to-right"):
    # Initialize the reverse flag and sort index
    reverse = False
    i = 0

    # Handle if we need to sort in reverse
    if method == "right-to-left" or method == 'bottom-to-top':
        reverse = True

    # Handle if we are sorting against the y-coordinate 
    # rather than the x-coordinate of the bounding box
    if method == "top-to-bottom" or method == 'bottom-to-top':
        i = 1

    # Construct the list of bounding boxes and sort them from top to bottom
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes), 
        key=lambda b:b[1][i], reverse=reverse))

    # Return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)


# Sort all the contours by top to bottom
contours, boundingBoxes = sort_contours(contours, method='top-to-bottom')


# Retrieve the cells position
# Creating a list of heights for all detected boxes
heights = [boundingBoxes[i][3] for i in range(len(boundingBoxes))]

# Get mean of heights
mean = np.mean(heights)

# Create list box to store all boxes in
box = []

# Get position (x, y), width and weight for every contour and show 
# the contour on image
for c in contours:
    x, y, w, h = cv2.boundingRect(c)

    if (w<1000 and h<1000):
        image = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        box.append([x, y, w, h])

plotting = plt.imshow(image, cmap='gray')
plt.show()


# Creating two lists to define row and column in which cell is located
row = []
column = []
j = 0


'''
We need to know in which row and which column it is located. As long as 
a box does not differ more than its own (height + mean/2) the box is in
same row. As soon as the height difference is higher than the current
(height + mean/2), we kown that a new row starts. 

Columns are logically arranged from left to right.
'''
# Sorting the boxes to their respective row and column
for i in range(len(box)):
    if(i==0):
        column.append(box[i])
        previous = box[i]

    else:
        if(box[i][1] <= previous[1]+mean/2):
            column.append(box[i])
            previous=box[i]

            if(i==len(box)-1):
                row.append(column)

        else:
            row.append(column)
            column=[]
            previous = box[i]
            column.append(box[i])

print(column)
print(row)

# Calculating maximum number of cells
countcol = 0
for i in range(len(row)):
    countcol = len(row[i])
    if countcol > countcol:
        countcol = countcol

# Retrieving the center of each column
center = [int (row[i][j][0] + row[i][j][2]/2) 
             for j in range(len(row[i])) if row[0]]

center = np.array(center)
center.sort()


# Regarding the distance to the columns center, the boxes are 
# arranged in respective order
finalboxes = []

for i in range(len(row)):
    lis = []
    for k in range(countcol):
        lis.append([])
    for j in range(len(row[i])):
        diff = abs(center - (row[i][j][0] + row[i][j][2]/4))
        minimum  = min(diff)
        indexing = list(diff).index(minimum)
        lis[indexing].append(row[i][j])

    finalboxes.append(lis)

# Extract values
# From every single image-based cell/box the strings are extracted via
# pytesseract and stored in a list
outer = []
for i in range(len(finalboxes)):
    for j in range(len(finalboxes[i])):
        inner = ''
        if(len(finalboxes[i][j]) == 0):
            outer.append(' ')

        else:
            for k in range(len(finalboxes[i][j])):
                y, x, w, h = finalboxes[i][j][k][0], finalboxes[i][j][k][1], \
                      finalboxes[i][j][k][2], finalboxes[i][j][k][3]
                finalImg = bitnot[x:x+h, y:y+w]
                kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 1))
                border = cv2.copyMakeBorder(finalImg, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=[255, 255])
                resizing = cv2.resize(border, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
                dilation = cv2.dilate(resizing, kernel, iterations=1)
                erosion = cv2.erode(dilation, kernel, iterations=1)

                out = pytesseract.image_to_string(erosion)
                if(len(out) == 0):
                    out = pytesseract.image_to_string(erosion, config='--psm 3')

                inner = inner + ' ' + out

            outer.append(inner)

# Creating a datafram of the generated OCR list
arr = np.array(outer)
dataframe = pd.DataFrame(arr.reshape(len(row), countcol))
print(dataframe)
data = dataframe.style.set_properties(align="left")

# Converting it in a excel-file
outputExcelFile = os.path.join(OUTPUT_DIR, 'output.xlsx')
data.to_excel(outputExcelFile, engine='xlsxwriter')
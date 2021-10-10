import cv2
import numpy as np

img = cv2.imread(r'C:\Users\xq127\Desktop\4.jpg')

width, height = 650, 900

pts1 = np.float32([[88, 481], [821, 466], [113, 1665], [877, 1634]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

for x in range(0, 4):
    cv2.circle(img, (int(pts1[x][0]), int(pts1[x][1])), 5, (0, 0, 255), cv2.FILLED)

cv2.imshow("Original Image ", img)
cv2.imshow("Output Image ", imgOutput)
cv2.imwrite(r'C:\Users\xq127\Desktop\warpPerspective.jpg', imgOutput)
cv2.waitKey(0)
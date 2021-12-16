import cv2
import  numpy as np
import os
import glob

DIRECTORY = r'C:\Users\xq127\Downloads\pictures\concatenateImgVertically'

# Scan imgs in DIRECTORY, order files by time
os.chdir(DIRECTORY)
imgs = os.listdir(DIRECTORY)
imgs.sort(key=lambda x: os.path.getmtime(x))

# concatenate imgs
def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [cv2.resize(im, (w_min, int(im.shape[0] * w_min / im.shape[1])), interpolation=interpolation)
                      for im in im_list]
    return cv2.vconcat(im_list_resize)

file = imgs[1]
print(os.path.abspath(file))

img_list = [cv2.imread(os.path.abspath(img)) for img in imgs]

# for img in img_list:
#     cv2.imshow('image', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

im_v_resize = vconcat_resize_min(img_list)
# os.chdir(DIRECTORY)
cv2.imwrite('opencv_vconcat_resize.jpg', im_v_resize)
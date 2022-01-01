import cv2
import numpy as np
import os
import glob
import shutil
import argparse

parser = argparse.ArgumentParser(description="指定图片要移到的目录")
parser.add_argument("targetFold", type=str, help="指定图片要移到的目录")
args = parser.parse_args()
targetFold = args.targetFold

originalPath = r"C:\Users\xq127\Downloads\pictures\synopsisImgDir"
destinationPath = os.path.join(
    r"D:\bookStore\productData", targetFold, "detailImageDir"
)


# Scan imgs in DIRECTORY, order files by time
os.chdir(originalPath)
img_type = ("*.jpg", "*.png")
img_grabbed = []
for files in img_type:
    img_grabbed.extend(glob.glob(files))

# Sort imgs by timestamp
img_grabbed.sort(key=os.path.getctime)

# concatenate imgs
def vconcat_resize_min(im_list, interpolation=cv2.INTER_CUBIC):
    w_min = min(im.shape[1] for im in im_list)
    im_list_resize = [
        cv2.resize(
            im,
            (w_min, int(im.shape[0] * w_min / im.shape[1])),
            interpolation=interpolation,
        )
        for im in im_list
    ]
    return cv2.vconcat(im_list_resize)


img_list = [
    cv2.imread(os.path.abspath(img))
    for img in sorted(img_grabbed, key=os.path.getctime)
]

# for img in img_list:
#     cv2.imshow('image', img)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

# Remove destination path
for filename in os.listdir(destinationPath):
    file_path = os.path.join(destinationPath, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print("Failed to delete %s. Reason: %s" % (file_path, e))


im_v_resize = vconcat_resize_min(img_list)
# os.chdir(DIRECTORY)
outputImg = os.path.join(destinationPath, "detailImage.jpg")
cv2.imwrite(outputImg, im_v_resize)

# Remove original image in original path
for filename in os.listdir(originalPath):
    file_path = os.path.join(originalPath, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print("Failed to delete %s. Reason: %s" % (file_path, e))

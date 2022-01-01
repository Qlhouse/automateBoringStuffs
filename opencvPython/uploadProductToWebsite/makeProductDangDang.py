import tkinter as tk
import tkinter.font as tkFont
import shutil
import os
import cv2
import numpy as np
import glob
import requests
from bs4 import BeautifulSoup

master = tk.Tk(className="移动图片")
master.geometry("800x600")
master["bg"] = "#ffbf00"

inputFontStyle = tkFont.Font(family="Lucida Grande", size=30)


inputPrompt = tk.Label(master, text="目标文件夹名称", bg="#6ffc03", font=inputFontStyle)
inputPrompt.place(relx=0.2, rely=0.1, anchor="center")

# 用户输入栏
inputText = tk.Entry(master, font=inputFontStyle)
inputText.place(relx=0.7, rely=0.1, anchor="center")


def moveBriefImgs():
    targetDir = inputText.get()

    originalPath = r"C:\Users\xq127\Downloads\pictures\synopsisImgDir"
    destinationPath = os.path.join(
        r"D:\bookStore\productData", targetDir, "synopsisImgDir"
    )

    # Remove original image in destinationPath
    for filename in os.listdir(destinationPath):
        file_path = os.path.join(destinationPath, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s" % (file_path, e))

    for file in os.scandir(originalPath):
        # shutil.move(file.path, os.path.join(destinationPath, file.name))
        shutil.move(file.path, destinationPath)


def moveDetialImgs():
    targetDir = inputText.get()

    originalPath = r"C:\Users\xq127\Downloads\pictures\synopsisImgDir"
    destinationPath = os.path.join(
        r"D:\bookStore\productData", targetDir, "detailImageDir"
    )

    # Scan imgs in originalPath, order files by time
    os.chdir(originalPath)
    img_type = ("*.jpg", "*.png")
    img_grabbed = []
    for fileType in img_type:
        img_grabbed.extend(glob.glob(fileType))

    # Sort imgs by timestamp
    img_grabbed.sort(key=os.path.getctime)
    print(img_grabbed)

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
        cv2.imdecode(
            np.fromfile(os.path.abspath(img), dtype=np.uint8), cv2.IMREAD_COLOR
        )
        for img in img_grabbed
    ]
    # for img in img_list:
    # cv2.imshow("image", img)
    # cv2.waitKey(0)

    # Remove original image in destinationPath
    for filename in os.listdir(destinationPath):
        file_path = os.path.join(destinationPath, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s" % (file_path, e))

    concatenatedImg = vconcat_resize_min(img_list)
    # os.chdir(DIRECTORY)
    outputImg = os.path.join(destinationPath, "detailImage.jpg")
    cv2.imwrite(outputImg, concatenatedImg)

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


def downloadConcatenateImgs():
    targetDir = inputText.get()

    imgLinksFile = r"D:\bookStore\productData\productDetial.html"

    destinationPath = os.path.join(
        r"D:\bookStore\productData", targetDir, "detailImageDir"
    )

    # Remove original image in destinationPath
    for filename in os.listdir(destinationPath):
        file_path = os.path.join(destinationPath, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print("Failed to delete %s. Reason: %s" % (file_path, e))

    imgLinkList = []
    imgList = []
    # Read image html document
    with open(imgLinksFile, "r") as imgText:
        soup = BeautifulSoup(imgText, "html.parser")
        imgTag = soup.find("img")
        imgLinkList.append(imgTag["src"])
        while imgTag.next_sibling:
            imgTag = imgTag.next_sibling
            imgLinkList.append(imgTag["src"])

    for link in imgLinkList:
        if link.endswith((".jpg", ".png")):
            resp = requests.get(link, stream=True).raw
            img = np.asarray(bytearray(resp.read()), dtype=np.uint8)
            imgList.append(cv2.imdecode(img, -1))

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

    im_v_resize = vconcat_resize_min(imgList)
    # print(outFileName)
    imgOutputName = os.path.join(destinationPath, "detailImage.jpg")

    cv2.imwrite(imgOutputName, im_v_resize)

    # Remove text in productDetial.html
    with open(imgLinksFile, "r+") as fh:
        fh.truncate(0)


buttomFontStyle = tkFont.Font(family="Lucida Grande", size=35)

# 按键
BriefImgs = tk.Button(
    text="移动简介图", font=buttomFontStyle, fg="#000fff", command=moveBriefImgs
)
BriefImgs.place(relx=0.5, rely=0.4, anchor="center")
# BriefImgs.

# DetialImgs = tk.Button(
#     text="移动详情图", font=buttomFontStyle, fg="#000fff", command=moveDetialImgs
# )
downloadConcatenateImgs
DetialImgs = tk.Button(
    text="移动详情图", font=buttomFontStyle, fg="#000fff", command=downloadConcatenateImgs
)
DetialImgs.place(relx=0.5, rely=0.65, anchor="center")

master.mainloop()

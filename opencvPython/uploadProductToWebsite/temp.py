import os

# targetDir = os.getcwd()
targetDir = os.path.dirname(os.path.realpath(__file__))

# briefImageDir = os.path.join(targetDir, "synopsisImgDir", "")
# briefImageDir = targetDir + "\\synopsisImgDir"
# print(briefImageDir)
# os.chdir(briefImageDir)
# briefImages = os.listdir(briefImageDir)

for entry in os.scandir(targetDir):
    # print(os.path.abspath(img))
    if entry.is_dir():
        print(entry.path)



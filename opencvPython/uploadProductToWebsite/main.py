import os
import json
from uploadProduct import uploadProduct, loginWeb, driver
from datetime import datetime
import logging
import shutil

productBackupDir = r"D:\bookStore\productDataBackup"
productData = r"D:\bookStore\productData"
dirList = []

logging.basicConfig(
    filename="failure.txt",
    filemode="w",
    format="%(asctime)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)

# 登录网站账户和密码
certificateFile = "certification.json"
with open(certificateFile, "r", encoding="utf-8") as userInfo:
    certification = json.load(userInfo)

loginWeb(certification)

for entry in os.scandir(productData):
    try:
        if entry.is_dir():
            uploadProduct(entry.path)
            dirList.append(entry.path)

    except Exception as e:
        logging.exception(f"Upload {os.path.basename(entry.path)} failed")
    finally:
        driver.close()

for dirpath in dirList:
    try:
        shutil.move(entry.path, productBackupDir)
    except Exception as e:
        logging.exception(f"Move {os.path.basename(entry.path)} failed")

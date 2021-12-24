import os
import json
from uploadProduct import uploadProduct  # , driver
from datetime import datetime
import logging

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

productData = r"D:\bookStore\productData"
for entry in os.scandir(productData):
    try:
        if entry.is_dir():
            # print(entry.path)
            uploadProduct(entry.path, certification)
    except Exception as e:
        logging.exception(f"Upload {os.path.basename(entry.path)} failed")
    # finally:
    #     driver.close()
    # if entry.is_dir():
    #     # print(entry.path)
    #     uploadProduct(entry.path, certification)

from PIL import Image
import os
import json
from pathlib import Path
import requests
from requests.api import head
from requests.sessions import session

def cropImage(imageAddress):
    print(imageAddress)
    # Open a image in RGB mode
    # In Windows, address should be raw text
    im = Image.open(imageAddress)

    # Setting the points for cropped image
    left = 0
    top = 207
    right = 450
    bottom = 848

    # Croped image of above dimension
    # It will not change original image
    im1 = im.crop((left, top, right, bottom))

    # Show the image in image viewer
    # imageOutputAddress = 'outputAddress'
    im1.save(imageAddress, quality=95)

# Traverse image files, crop file in turn
def cropFileInTurn(directory):
    # In windows, directory should be in raw text, r'C:\Users\xq127\Pictures\temp'
    for dirpath, dirnames, filenames in os.walk(directory):
        dir = Path(dirpath)
        for file in filenames:
            file = dir / file
            cropImage(file)

# Upload image file to sm.ms(https://sm.ms/)
'''
def uploadImage(path):
    headers = {'Authorization': '5NUSX0M5dr3ewDHK5x8cqpfCCMHfB6e4'}
    files = {'smfile': open(path, 'rb')}
    url = 'https://sm.ms/api/v2/upload'
    res = requests.post(url, files=files, headers=headers).json()
    print(json.dumps(res, indent=4))
'''

def uploadImage(path):
    # session 
    api_addr = 'https://sm.ms/api/v2'
    upload_api = '/upload'
    url = api_addr + upload_api
    # headers = {'Authorization': '5NUSX0M5dr3ewDHK5x8cqpfCCMHfB6e4'}
    files = {'smfile': open(path, 'rb')}
    res = requests.post(url, files=files)
    print(res)
    resp = res.json()
    print(json.dumps(res, indent=4))

path = Path(r'C:\Users\xq127\Pictures\temp\CE9C20A44CDBFD9FEF2C3B71F478A1BB.jpg')
uploadImage(path)
# cropFileInTurn(r'C:\Users\xq127\Pictures\temp')
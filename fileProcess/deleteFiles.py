import re
import os

filesDir = 'H:\\convolution\\'

def deleteFile():
    for file in os.listdir(filesDir):
        if file.endswith('.srt'):
            # Pattern: '\.ko'. Replace pattern here.
            if re.search('\.ko' ,file):
                # print(file)
                os.remove(filesDir + file)

deleteFile()
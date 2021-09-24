import re
import os

# extension check
# endswith('.mp4)

# os.chdir('Dir) Change directory
# os.listdir('srcDir') Return list of all content if Dir
# os.rename(src, dst)

filesDir = 'D:\\kivy'

for file in os.listdir(filesDir):
    if file.endswith('.mp4') or file.endswith('.webm'):
        # print(file)
        try:
            order = re.search('#\d+', file)
        except AttributeError:
            order = 'Not found'
        
        if order != None:
            newFileName = order.group() + '-' + file
            src = filesDir + '\\' + file
            dst = filesDir + '\\' + newFileName
            os.rename(src, dst)

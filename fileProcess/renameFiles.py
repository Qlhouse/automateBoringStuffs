import re
import os

# extension check
# endswith('.mp4)

# os.chdir('Dir) Change directory
# os.listdir('srcDir') Return list of all content if Dir
# os.rename(src, dst)

filesDir = 'D:\\kivy'

def renameVedios():
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

def renameSrt():
    for file in os.listdir(filesDir):
        if file.endswith('.srt'):
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

renameSrt()

def rename(dir):
    for item in os.listdir(dir):
        entry = os.path.join(dir, item)
        if os.path.isfile(entry):
            if item.endswith(".srt"):
                newBasename = item.replace('-en_US', '')
                newEntry = os.path.join(dir, newBasename)
                shutil.move(entry, newEntry)

        if os.path.isdir(item):
            rename(os.path.abspath(item))


dir = r'C:\迅雷下载\[FreeCourseSite.com] Udemy - Mastering 4 critical SKILLS using Python'
os.chdir(dir)
rename(dir)


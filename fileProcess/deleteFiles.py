import re
import os

# filesDir = input("Please input the root directory: ")
# pattern = input("Please input file endswith")


def deleteFile(dir, pattern):
    print("Begin")
    for item in os.scandir(dir):
        # 　:
        if item.is_file():
            if item.name.endswith(pattern):
                # print("FILE")
                # Pattern: '\.ko'. Replace pattern here.
                # if re.search('\.ko', file):
                # print(file)
                os.remove(item)
        elif item.is_dir():
            print(item.path)
            # print("DIRECTORY")
            deleteFile(item.path, pattern)
        else:
            print("WRONG")


deleteFile(r'C:\Users\Administrator\Downloads', '.m4a')

import os
from datetime import datetime

# currentTimestamp = datetime.today().strftime('%Y%m%d%H%M%S')

folder = r'C:\Users\xq127\Pictures\uploadImage'

def renameFiles(folder):
    id = 1
    for file in os.listdir(folder):
        oldName = os.path.join(folder, file)
        newBase = str(id) + '_new' + '.jpg'
        newName = os.path.join(folder, newBase)
        os.rename(oldName, newName)
        id += 1
        
if __name__ == '__main__':
    renameFiles(folder)

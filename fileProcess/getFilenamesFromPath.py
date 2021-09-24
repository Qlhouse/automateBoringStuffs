import os
import os.path

# scan the directory, choose certain , get file name.

# os.path.splitext()

# os.path.basename()

indexFile = r'D:\kivy\index.txt'
objectDir = r'D:\kivy'

if os.path.exists(indexFile):
    with open(indexFile, 'w') as fh:
        fh.truncate()
else:
    with open(indexFile, 'w') as fh:
        pass


for file in os.listdir(objectDir):
    if file.endswith('.mp4'):
        with open(indexFile, 'ab+') as fh:
            file = file.encode('utf-8')
            fh.write(file)
            fh.write('\n'.encode('utf-8'))

    elif file.endswith('.webm'):
        with open(indexFile, 'a+') as fh:
            fh.write(str(file))
            fh.write('\n')

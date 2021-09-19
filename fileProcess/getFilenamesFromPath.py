import os
import os.path

# scan the directory, choose certain , get file name.

# os.path.splitext()

# os.path.basename()

indexFile = r'D:\linearAlgebra\index.txt'

if os.path.exists(indexFile):
    with open(indexFile, 'w') as fh:
        fh.truncate()
else:
    with open(indexFile, 'w') as fh:
        pass


for file in os.listdir(r'D:\linearAlgebra'):
    if file.endswith('.mp4'):
        with open(indexFile, 'a+') as fh:
            file = file.encode('utf-8')
            fh.write(str(file))
            fh.write('\n')

    elif file.endswith('.webm'):
        with open(indexFile, 'a+') as fh:
            fh.write(str(file))
            fh.write('\n')

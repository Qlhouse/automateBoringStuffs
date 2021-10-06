import os
from posixpath import basename

absRootPath = os.path.abspath(__file__)
# print(rootPath)

BASE_DIR = os.path.dirname(absRootPath)
# print(BASE_DIR)

SOURCE_DIR = os.path.join(BASE_DIR, 'source')

OUTPUT_DIR = os.path.join(BASE_DIR, 'output')
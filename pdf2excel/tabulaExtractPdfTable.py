'''
# Install camelot
$ pip install "camelot-py[cv]"

# Note
Camelot only works on text-based pages, 
doesn't work on image-based pdf.
'''

import camelot

tables = camelot.read_pdf(r'C:\Users\xq127\Documents\Scan\sdsdsfdsfd.pdf')
print(tables[0].df)
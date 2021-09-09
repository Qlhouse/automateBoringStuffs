'''
[Refer sites]
![camelot](https://github.com/atlanhq/camelot)

![pdfplumber](https://github.com/jsvine/pdfplumber)

![tabulapdf](https://github.com/tabulapdf/tabula)

![pdftables](https://pdftables.com/)
'''

'''
# Install pdfplumber
pip install pdfplumber
'''

import pdfplumber

pdf = pdfplumber.open(r'C:\Users\xq127\Desktop\primarySchoolEssentialBooks.pdf')

page = pdf.pages[1]

text = page.extract_tables()

print(text)
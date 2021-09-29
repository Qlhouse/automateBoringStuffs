import requests
import ftplib

from requests.sessions import session

URL = 'https://api.streamsb.com/api'

KEY = '23149ggar73ufc5wewgw1'

def accountInfo(key):
    url = URL + f'/account/info?key={key}'
    res = requests.get(url)
    print(res.text)

# accountInfo(KEY)

# FTP_HOST = 'ftp://ftp.streamsb.com/'
FTP_HOST = 'ftp.microsoft.com'
FTP_USER = 'qlinpy'
FTP_PASS = 'fsd472yi0z'

ftp = ftplib.FTP(FTP_HOST)
ftp.login(FTP_USER, FTP_PASS)

'''
ftp.encoding = 'uft-8'
ftp.dir()
'''

'''
import socket
print(socket.getaddrinfo('localhost', 8080))
'''
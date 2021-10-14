import requests
from bs4 import BeautifulSoup

url = 'https://www.amazon.com/Roku-Express-Streaming-Wireless-Controls/dp/B0916TKFF2/ref=lp_16225009011_1_11?dchild=1'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}

r = requests.get(url, headers=headers)

with open('web.html', 'wb') as fh:
    fh.write(r.content)

print(r.status_code)

soup = BeautifulSoup(r.content, features='lxml')

price = soup.find('span', {'id': 'priceblock_ourprice'}).text
print(price)
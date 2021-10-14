from requests_html import HTMLSession
from bs4 import BeautifulSoup

searchitem = 'dslr+card'
url = f'https://www.amazon.com/s?k={searchitem}&qid=1634207861&ref=sr_pg_1'

s = HTMLSession()

def getData(url):
    r = s.get(url)
    r.html.render(sleep=1, timeout=80)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

def getDetails(soup):
    products = soup.find_all('div', {'data-component-type': "sp-sponsored-result"})
    for item in products:
        link = item.find('a', {'class': 'a-link-normal a-text-normal'})
        print(link)

getDetails(getData(url))['href']
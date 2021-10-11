# Synchronous scraper
'''
from requests_html import HTMLSession
import time

urls = []
for x in range(1, 51):
    urls.append(f'https://books.toscrape.com/catalogue/page-{x}.html')

# print(len(urls))

def work(url):
    r = s.get(url)
    products = []
    desc = r.html.find('article.product_pod')
    for item in desc:
        product = {
            'title': item.find('h3 a[title]', first=True).text,
            'price': item.find('p.price_color', first=True).text
        }
        products.append(product)
    
    return products

def main(urls):
    for url in urls:
        print(work(url))
    return

s = HTMLSession()
start = time.perf_counter()
main(urls)
fin = time.perf_counter() - start
print(fin)

# Spend time: 25.0937527 
'''

# Asynchronous scraper
'''
Python coroutines are awaitables
and therefore can be awaited from other coroutines
ASYNC DEF / AWAIT

Event Loop - this runs the tasks and controls the network
subprocesses. We do not need to reference the loop directly, 
instead favouring asyncio.run() to execute the coroutines.

Tasks - these are used to run the coroutines in the event loop.
'''

from requests_html import AsyncHTMLSession
import asyncio
import time

urls = []
for x in range(1, 51):
    urls.append(f'https://books.toscrape.com/catalogue/page-{x}.html')

print(len(urls))

async def work(s, url):
    r = await s.get(url)
    products = []
    desc = r.html.find('article.product_pod')
    for item in desc:
        product = {
            'title': item.find('h3 a[title]', first=True).text,
            'price': item.find('p.price_color', first=True).text
        }
        products.append(product)
    
    return products

async def main(urls):
    s = AsyncHTMLSession()
    tasks = (work(s, url) for url in urls)
    return await asyncio.gather(*tasks)

start = time.perf_counter()
results = asyncio.run(main(urls))
print(results)
fin = time.perf_counter() - start
print(fin)

# Spend time: 11.7878431
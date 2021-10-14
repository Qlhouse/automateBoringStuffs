from requests_html import HTMLSession
import pandas as pd
import time

s = HTMLSession()
drinkList = []

def request(url):
    r = s.get(url)
    r.html.render(sleep=1, timeout=30000)
    # print(r.status_code)
    return r.html.find('div#product-items-container', first=True)

def parse(products):
    for item in products.absolute_links:
        try:
            # print(item, sep='->')
            r = s.get(item)
            name = r.html.find('div.product-detail-info-title', first=True).text
            subtext = r.html.find('div.product-subtext', first=True).text
            price = r.html.find('span.price', first=True).text
            try:
                rating = r.html.find('span.label-stars', first=True).text
            except:
                rating = 'None'
        
            if r.html.find('div.add-to-cart-container'):
                stock = 'in stock'
            else:
                stock = 'out of stock'
            
            drink = {
                'name': name, 
                'subtext': subtext, 
                'price': price,
                'rating': rating, 
                'stock': stock,
            }

            drinkList.append(drink)
        except AttributeError:
            print('No matched find')

def output():
    df = pd.DataFrame(drinkList)
    df.to_csv('beer.csv', index=False)
    print('Saved to CSV file')


x = 1
while True:
    try:
        products = request(f'https://www.beerwulf.com/en-gb/c?routeQuery=c&page={x}')
        print(f'Getting items from page {x}.')
        parse(products)
        print('Total Items: ', len(drinkList))
        x += 1
        time.sleep(6)
    except:
        print('No more items!')
        break

output()
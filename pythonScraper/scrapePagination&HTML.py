import requests
from bs4 import BeautifulSoup
import time
import pandas as pd


holidayHomes = []

for x in range(1, 54):
    url = f'https://www.brittany-ferries.co.uk/holidays/search?vt=0&s=ASC&p={x}'
    
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content, 'html.parser')
    
    content = soup.find_all('dd-product-card', class_='product product-grid ng-star-inserted')
    
    for property in content:
        name = property.find('h2').text
        houseType = property.find('h3').text
        price = property.find('p').text
        city = property.find('p', class_='breadcrumb').text
        # ref = property.find('p', class_='reference').text
        property_info = {
            'name': name, 
            'houseType': houseType, 
            'price': price, 
            'city': city
        }
        holidayHomes.append(property_info)
    time.sleep(3)

df = pd.DataFrame(holidayHomes)
print(df.head())

df.to_csv('holidayHomes.csv', index=False)
print('Saved to CSV file')
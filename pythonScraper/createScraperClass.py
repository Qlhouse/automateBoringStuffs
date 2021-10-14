from requests_html import HTMLSession

class Scraper:
    def __init__(self):
        self.session = HTMLSession()
        self.headers = {'User-Agaent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
        self.baseUrl = 'https://www.amazon.co.uk/Piece-Computer-Repair-Tool-Kit/dp/'

    def extract(self, asin):
        r = self.session.get(self.baseUrl + str(asin), headers=self.headers)
        scraped_item = (
            r.html.find('span#productTitle', first=True).text, 
            r.html.find('span#priceblock_ourprice', first=True).text,
        )

        return scraped_item

if __name__ == '__main__':
    plzsub = Scraper()
    product = plzsub.extract('B0033MHUAA')
    print(product)
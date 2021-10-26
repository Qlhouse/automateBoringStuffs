import  requests
import  json
from bs4 import BeautifulSoup
from lxml.html import fromstring

class YTstats:
    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_statistics = None

    @classmethod
    def get_proxies(cls):
        url = 'https://free-proxy-list.net/'
        response = requests.get(url)
        parser = fromstring(response.text, 'lxml')
        proxies = set()
        for i in parser.xpath('//tbody/tr')[:100]:
            if i.xpath('.//td[7]/text()')[0] == "yes":
                # Grabbing IP and corresponding PORT
                proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                proxies.add(proxy)

        return proxies

    def get_channel_statistics(self):
        url = f'https://www.googleapis.com/youtube/v3/channels?part=statistics&id={self.channel_id}&key={self.api_key}'
        # print(url)
        proxies = {
            "http":'http://ubuntu:Ql@19630109@101.32.194.157:8080/',
            "https":'https://ubuntu:Ql@19630109@101.32.194.157:8080/'
        }
        json_url = requests.get(url, proxies=proxies)
        data = json.loads(json_url.text)
        print(data)
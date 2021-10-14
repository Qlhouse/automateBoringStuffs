from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://www.sina.com.cn/')

# print(dir(r.html.links))
# about = r.html.find('#yesnojs', first=True)
# print(about.text)

r.html.render(timeout=20)
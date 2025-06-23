from bs4 import BeautifulSoup
import requests as r

url= 'https://quotes.toscrape.com/'

html = r.get(url)

soup=BeautifulSoup(html.text,'lxml')
type= soup.find_all('span',class_='text')
for tag in type:
    print(tag.text.strip())
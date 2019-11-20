from requests import get
from bs4 import BeautifulSoup

url = 'https://www.ozbargain.com.au/'
response = get(url, headers={'User-Agent': 'Mozilla/5.0'})
html= response.content

soup = BeautifulSoup(html)
print(soup.prettify())

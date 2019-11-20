from requests import get
from bs4 import BeautifulSoup


class Scraper:

    def __init__(self, url):
        response = get(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = response.content
        self.data = BeautifulSoup(html, features="html5lib")
        self.nodes = self.data.findAll(
                'div',
                attrs={'class': lambda L: L
                       and L.find("node-ozbdeal") > 0
                       and L.find("expired") == -1}
                )

    def count(self):
        return len(self.nodes)

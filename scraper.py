from requests import get
from bs4 import BeautifulSoup


class Scraper:

    def __init__(self, url):
        response = get(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = response.content
        self.data = BeautifulSoup(html, features='html.parser')
        self.nodes = self.extractRow(self.data)

        self.table = []

        for node in self.nodes:
            self.table.append(self.extractData(node))

    def extractRow(self, data):
        return data.findAll(
                'div',
                attrs={'class': lambda L: L
                       and L.find("node-ozbdeal") > 0
                       and L.find("expired") == -1}
                )

    def extractData(self, node):
        result = []
        title_section = node.find('h2', attrs={'class': 'title'})
        title = title_section.get('data-title')
        result.append(title)
        content_section = node.find('div', attrs={'class': 'content'})
        content = content_section.get_text().strip()
        result.append(content)
        return result

    def count(self):
        return len(self.nodes)

    def print_table(self):
        for row in self.table:
            print('TITLE')
            print(row[0])
            print('CONTENT')
            print(row[1])

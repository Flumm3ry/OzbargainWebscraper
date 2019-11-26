from requests import get
from bs4 import BeautifulSoup
from node import Node


class Scraper:

    def __init__(self, url):
        self.url = url
        response = get(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = response.content
        self.data = BeautifulSoup(html, features='html.parser')
        self.rows = self.extractRow(self.data)

        self.table = []

        for row in self.rows:
            self.table.append(self.extractData(row))

    def extractRow(self, data):
        return data.findAll(
                'div',
                attrs={'class': lambda L: L
                       and L.find("node-ozbdeal") > 0
                       and L.find("expired") == -1}
                )

    def extractData(self, row):
        title_section = row.find('h2', attrs={'class': 'title'})
        title = title_section.get('data-title')
        node_num = title_section.find('a').get('href').split("/")[-1:]
        op_link = self.url + "node/" + node_num[0] 
        deal_link = self.url + "goto/" + node_num[0]
        content_section = row.find('div', attrs={'class': 'content'})
        content = content_section.get_text().strip()
        return Node(title, content, op_link, deal_link)

    def count(self):
        return len(self.rows)

    def get_html_results(self):
        result = ""
        for node in self.table:
            result = result + node.get_html()
        return result

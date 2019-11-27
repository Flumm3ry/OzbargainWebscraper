from requests import get
from bs4 import BeautifulSoup
from node import Node
import os


class Scraper:

    def __init__(self, url):
        self.url = url
        response = get(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = response.content
        self.data = BeautifulSoup(html, features='html.parser')
        self.rows = self.extractRow(self.data)

        self.nodes = []

        for row in self.rows:
            self.nodes.append(self.extractData(row))

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
        content_section = row.find('div', attrs={'class': 'content'})
        content = content_section.get_text().strip()
        return Node(title, content, node_num[0])

    def updateCSV(self, filename):
        l_node_num = 0

        if not os.path.exists('data'):
            os.makedirs('data')
            open('data/'+filename, 'x').close()

        f = open('data/'+filename, "r+")

        latest_node = f.readline()
        if latest_node:
            l_node_num = int(latest_node.split('|', 1)[0])

        f.seek(0, 0)

        print("nah")

        for node in self.nodes:
            if int(node.node_num) <= l_node_num:
                break
            print("yah")
            f.write(node.get_csv() + '\n')

        f.close()

from requests import get
from bs4 import BeautifulSoup
from node import Node
from node_list import NodeList
import os
from config import path_directory


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
        node_list = NodeList(filename='node_file.txt')

        node_list.nodes += self.nodes

        node_list.sort()
        node_list.remove_duplicates()

        if not os.path.exists(path_directory + 'data'):
            os.makedirs(path_directory + 'data')
            open(path_directory + 'data/'+filename, 'x').close()

        f = open(path_directory + 'data/'+filename, "w")
        
        lines = []

        for node in node_list.nodes:
            lines.insert(0, node.get_csv() + '\n')
        
        f.writelines(lines)

        f.close()

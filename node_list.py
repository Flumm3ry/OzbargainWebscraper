from node import Node


class NodeList:

    def __init__(self, filename):
        self.nodes = []

        f = open('data/' + filename, 'r')
        data = f.readlines()

        for line in data:
            arr = line.split('|')
            new_node = Node(arr[1], arr[2], arr[0])
            self.nodes.append(new_node)

        f.close()

    def get_html_results(self):
        result = ""
        for node in self.nodes:
            result = result + node.get_html()
        return result

    def count(self):
        return len(self.nodes)

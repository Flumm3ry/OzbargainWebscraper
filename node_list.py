from node import Node


class NodeList:

    def __init__(self, filename=None, nodes=None):
        # read nodes from file
        if (filename):
            self.nodes = []

            f = open('data/' + filename, 'r')
            data = f.readlines()

            for line in data:
                arr = line.split('|')
                if len(arr) == 3:
                    new_node = Node(arr[1], arr[2], arr[0])
                    self.nodes.append(new_node)

            f.close()

        else:
            self.nodes = nodes

    def get_html_results(self):
        result = ""
        for node in self.nodes:
            result = result + node.get_html()
        return result

    def count(self):
        return len(self.nodes)

    def remove_before(self, min_num):
        self.nodes = [nodes for nodes in self.nodes if int(nodes.node_num) > min_num]

    def sort(self):
        self.nodes.sort(key=lambda x: x.node_num)

    def remove_duplicates(self):
        result = []
        i = -1
        for node in self.nodes:
            if not node.node_num == i:
                result.append(node)
            i = node.node_num

        self.nodes = result

    def get_newest_node(self):
        if self.nodes[0]:
            return self.nodes[0].node_num
        else:
            return 0

    def search_list(self, search_term):
        
        result = []

        for node in self.nodes:
            if search_term in node.content.lower() or search_term in node.title.lower():
                result.append(node)

        return result


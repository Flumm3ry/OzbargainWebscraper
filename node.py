class Node:
    def __init__(self, title, content, node_num):
        base_url = "https://www.ozbargain.com.au/"
        self.title = title
        self.content = content
        self.op_link = base_url + 'node/' + str(node_num)
        self.deal_link = base_url + 'goto/' + str(node_num)
        self.node_num = node_num

    def get_html(self):
        result = "<div class='card'><div class='card-body'>"
        result = result + "<h5 class='card-title'>"
        result = result + self.title
        result = result + "</h5>"
        result = result + "<p class='card-text'>"
        result = result + self.content
        result = result + "</p>"
        result = result + "<a class='card-link' target='_blank' href='"
        result = result + self.deal_link
        result = result + "'>Link to Deal</a>"
        result = result + "<a class='card-link' target='_blank' href='"
        result = result + self.op_link
        result = result + "'>Link to Original Post</a>"
        result = result + "</div></div>"
        return result

    def get_csv(self):
        delimiter = '|'
        csv = self.node_num + delimiter
        csv = csv + self.title + delimiter
        csv = csv + self.content.replace(r'\n', "")

        return csv

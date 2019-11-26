class Node:
    def __init__(self, title, content, op_link, deal_link):
        self.title = title
        self.content = content
        self.op_link = op_link
        self.deal_link = deal_link

    def get_html(self):
        result = "<br>"
        result = result + "<p>"
        result = result + self.title
        result = result + "</p>"
        result = result + "<p>"
        result = result + self.content
        result = result + "</p>"
        result = result + "<p>"
        result = result + self.op_link
        result = result + "</p>"
        result = result + "<p>"
        result = result + self.deal_link
        result = result + "</p>"
        result = result + "<br>"
        return result

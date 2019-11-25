class Node:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_html(self):
        result = "<br>"
        result = result + "<p>"
        result = result + self.title
        result = result + "</p>"
        result = result + "<p>"
        result = result + self.content
        result = result + "</p>"
        result = result + "<br>"
        return result

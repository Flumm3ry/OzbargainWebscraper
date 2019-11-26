class Node:
    def __init__(self, title, content, link):
        self.title = title
        self.content = content
        self.link = link

    def get_html(self):
        result = "<br>"
        result = result + "<p>"
        result = result + self.title
        result = result + "</p>"
        result = result + "<p>"
        result = result + self.content
        result = result + "</p>"
        result = result + "<p>"
        result = result + self.link
        result = result + "</p>"
        result = result + "<br>"
        return result

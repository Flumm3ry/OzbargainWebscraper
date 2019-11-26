class Node:
    def __init__(self, title, content, op_link, deal_link):
        self.title = title
        self.content = content
        self.op_link = op_link
        self.deal_link = deal_link

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

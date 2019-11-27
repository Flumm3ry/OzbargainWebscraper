from scraper import Scraper
from flask import Flask, render_template
from node_list import NodeList

scraper = Scraper("https://www.ozbargain.com.au/")

scraper.updateCSV('node_file.txt')

node_list = NodeList(scraper.nodes)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", table=node_list.get_html_results())


@app.route("/alerts")
def alerts():
    return render_template("alerts.html")


print(str(node_list.count()) + ' nodes retrieved')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

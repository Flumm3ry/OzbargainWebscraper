from scraper import Scraper
from flask import Flask, render_template
from node_list import NodeList
from apscheduler.schedulers.background import BackgroundScheduler

url = "https://www.ozbargain.com.au/"

Scraper(url).updateCSV('node_file.txt')

node_list = NodeList(filename='node_file.txt')

app = Flask(__name__)


def update_scraped_data():
    Scraper(url).updateCSV('node_file.txt')
    global node_list
    node_list = NodeList('node_file.txt')


sched = BackgroundScheduler(daemon=True)
sched.add_job(update_scraped_data, 'interval', minutes=60)
sched.start()


@app.route("/")
def home():
    return render_template("home.html", table=node_list.get_html_results())


@app.route("/alerts")
def alerts():
    return render_template("alerts.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')

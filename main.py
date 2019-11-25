from scraper import Scraper
from flask import Flask, render_template

scraper = Scraper("https://www.ozbargain.com.au/")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", table=scraper.get_html_results())


print(scraper.count())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

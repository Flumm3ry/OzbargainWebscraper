from scraper import Scraper
from flask import Flask, render_template, request, session, redirect, url_for
from node_list import NodeList
from apscheduler.schedulers.background import BackgroundScheduler
import models as dbHandler

url = "https://www.ozbargain.com.au/"

#Scraper(url).updateCSV('node_file.txt')

node_list = NodeList(filename='node_file.txt')

app = Flask(__name__)
app.config['SECRET_KEY'] = "super secret key"


def update_scraped_data():
    #Scraper(url).updateCSV('node_file.txt')
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


@app.route("/login", methods=['GET', 'POST'])
def login():
    
    error = None

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # TODO: Sanitise input here
        user_id = dbHandler.log_in_user(email, password)
        if user_id:
            session['user'] = user_id
            return redirect(url_for('home'))
        else:
            error = "Incorrect login details"

    # Display form and error message (if any) here
    return render_template("login.html", err_msg = error)


@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host='0.0.0.0')

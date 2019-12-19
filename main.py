from scraper import Scraper
from flask import Flask, render_template, request, session, redirect, url_for
from flask_mail import Mail, Message
from node_list import NodeList
from apscheduler.schedulers.background import BackgroundScheduler
import models as dbHandler
from alert_list import AlertList
from config import mail_config
from passlib.hash import pbkdf2_sha256 as hasher

url = "https://www.ozbargain.com.au/"

Scraper(url).updateCSV('node_file.txt')

node_list = NodeList(filename='node_file.txt')

app = Flask(__name__)
app.config['SECRET_KEY'] = "super secret key"
app.config.update(mail_config)
mail = Mail(app)


def update_scraped_data():
    Scraper(url).updateCSV('node_file.txt')
    global node_list
    node_list = NodeList('node_file.txt')

def send_emails(to_email):
    for data in to_email:
        user = data[0]
        nodes = data[1]

        if nodes:
            message_content = "<p><b>Hey " + user.username + ",</b></p><br/>"
            message_content += "<p>We've found some bargains that match your alerts!</p>"

            for node in nodes:
                message_content += "<h6><a href=\"" + node.op_link + "\">" + node.title + "</a></h6>"

            with app.app_context():
                msg = Message(subject="Bargain Alert",
                              sender=app.config.get("MAIL_USERNAME"),
                              recipients=["user.email"],
                              html=message_content)
                mail.send(msg)


def check_alerts():
    alert_list = AlertList(dbHandler.get_all_alerts())

    to_check = alert_list.search_list(node_list)

    to_email = []

    for user_id, nodes in to_check:
           user = dbHandler.get_user(user_id)
           checked_nodes = []
           for node in nodes:
               if int(node.node_num) > user.last_alert_checked and node not in checked_nodes:
                   checked_nodes.append(node)

           to_email.append([user, checked_nodes])

    send_emails(to_email)

    dbHandler.update_last_alert(node_list.get_newest_node())


sched = BackgroundScheduler(daemon=True)
sched.add_job(update_scraped_data, 'interval', minutes=60)
sched.start()

check_alerts()


@app.route("/")
def home():
    logged_in_user = None
    if 'user_id' in session:
        logged_in_user = dbHandler.get_user(session['user_id'])
    return render_template("home.html", table=node_list.get_html_results(), user=logged_in_user)


@app.route("/alerts", methods=['GET', 'POST'])
def alerts():
    
    logged_in_user = None
    if 'user_id' in session:
        logged_in_user = dbHandler.get_user(session['user_id'])
    else:
        return "Error, user must be logged in to use this feature"
    
    if request.method == 'GET':
        to_delete = request.args.get('delete')
        # input will need to be sanitised here
        to_add = request.args.get('toAdd')
        
        if to_delete:
            dbHandler.delete_alert(to_delete)

        elif to_add:
            dbHandler.add_alert(to_add, logged_in_user.id)

    users_alerts = dbHandler.get_users_alerts(logged_in_user.id)
    return render_template("alerts.html", user=logged_in_user, alerts=users_alerts)


@app.route("/login", methods=['GET', 'POST'])
def login():
    
    error = None

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # TODO: Sanitise input here
        user_id = dbHandler.log_in_user(email, password)
        if user_id:
            session['user_id'] = user_id
            return redirect(url_for('home'))
        else:
            error = "Incorrect login details"

    # Display form and error message (if any) here
    return render_template("login.html", err_msg = error)


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    
    error = ""

    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_conf = request.form['password_conf']
        # TODO: Sanitise and validate input here
        if password != password_conf:
            error = "Please ensure passwords match"
        if not error:  
            dbHandler.insert_user(username, email, hasher.hash(password), node_list.get_newest_node())
            return redirect(url_for('login'))

    # Display form and error message (if any) here
    return render_template("signup.html", err_msg = error)


@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host='10.0.0.11')

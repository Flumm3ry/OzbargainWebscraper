import sqlite3 as sql
from user import User
from alert import Alert
from passlib.hash import pbkdf2_sha256 as hasher


def insert_user(username, email, password, alert_id):
    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username, email, password, last_alert_check) VALUES (?, ?, ?, ?)", (username, email, password, str(alert_id)))

    con.commit()
    con.close()

def is_unique_email(email):
    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM users WHERE email = ?", (email, ))
    
    if cur.fetchone():
        result = False
    else:
        result = True

    con.close()

    return result


def log_in_user(email, password):
    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("SELECT id, password FROM users WHERE email = ?", (email, ))

    user_data = cur.fetchone()
    
    con.close()

    if user_data:
        if (hasher.verify(password, user_data[1])):
            return user_data[0]

    return None


def get_user(user_id):
    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("SELECT id, username, email, last_alert_check FROM users WHERE id = ?", [str(user_id)])
    
    details = cur.fetchone()
    
    if details:
        user = User(details)
        con.close()

        return user
    else:
        con.close()
        return None


def update_last_alert(node_num):
    
    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("UPDATE users SET last_alert_check = ?", [str(node_num)])
    con.commit()
    con.close()


def get_all_alerts():

    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("SELECT id, user_id, alert FROM alerts")
    
    result = []

    for row in cur:
        result.append(Alert(alert_id=row[0], user_id=row[1], text=row[2]))
    
    con.close()

    return result


def get_users_alerts(user_id):

    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("SELECT id, alert FROM alerts WHERE user_id = ?", (str(user_id)))
    
    result = []

    for row in cur:
        result.append(Alert(alert_id=row[0], text=row[1]))
    
    con.close()

    return result


def delete_alert(alert_id):
    
    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("DELETE FROM alerts WHERE id = ?", (str(alert_id)))
    con.commit()
    con.close()


def add_alert(text, user_id):

    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("INSERT INTO alerts VALUES (NULL, ?, ?)", (str(user_id), str(text)))
    con.commit()
    con.close()

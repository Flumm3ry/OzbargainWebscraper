import sqlite3 as sql
from user import User


def insert_user(username, email, password, alert_id):
    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username, email, password, last_alert_check) VALUES (?, ?, ?, ?)", (username, email, password, str(alert_id)))

    con.commit()
    con.close()


def log_in_user(email, password):
    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("SELECT id FROM users WHERE email = ? AND password = ?", (email, password))

    user_id = cur.fetchone()
    
    con.close()

    if user_id:
        return user_id[0]
    else:
        return None


def get_user(user_id):
    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("UPDATE users SET last_alert_check = ?", (str(user_id)))
    
    con.close()

    details = cur.fetchone()

    if details:
        return User(details)
    else:
        return None

def update_last_alert(node_num)
    
    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("SELECT id, username, email FROM users WHERE id = ?", (str(node_num)))
    
    con.close()

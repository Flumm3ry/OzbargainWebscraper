import sqlite3 as sql
from user import User


def insert_user(username, email, password):
    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))

    con.commit()
    con.close()


def log_in_user(email, password):
    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("SELECT id FROM users WHERE email = ? AND password = ?", (email, password))

    user_id = cur.fetchone()

    if user_id:
        print(user_id[0][0])
        return user_id[0][0]
    else:
        return None


def get_user(user_id):
    con = sql.connect("data/scraper.db")
    cur = con.cursor()
    cur.execute("SELECT id, username, email FROM users WHERE id = ?", (user_id))

    user = cur.fetchone()
    
    if user:
        return User(user)

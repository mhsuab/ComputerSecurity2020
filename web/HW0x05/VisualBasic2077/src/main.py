#!/usr/bin/env python3
from os import getenv, urandom
from flask import Flask, g, request, session, send_file
import sqlite3

app = Flask(__name__)
app.secret_key = urandom(32)


class Flag():
    def __init__(self, flag):
        self.flag = flag
    def __str__(self):
        return self.flag if session.get('is_admin', False) else "Oops, You're not admin (・へ・)"


def db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('sqlite.db')
        db.row_factory = sqlite3.Row
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index():
    session['is_admin'] = False
    return send_file("index.html")

@app.route("/hint")
def hint():
    _='_=%r;return (_%%_)';return (_%_)

@app.route('/login', methods=["POST"])
def login():
    flag = Flag(getenv("FLAG", 'NOTFLAG{TEST}'))
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    cursor = db().cursor()
    query = f"select username, password from users where username='{username}' and password='{password}'"
    cursor.execute(query)
    res = cursor.fetchone()

    if res != None:
        print (f"username = {res['username']}, password = {res['password']}")

    if res != None and res['username'] == username and res['password'] == password:
        return ("<h1>Hello, " + username + " ｡:.ﾟヽ(*´∀`)ﾉﾟ.:｡ </h1> Here is your flag: {flag} ").format(flag=flag)
    else:
        print (flag.flag)
        resp = ''

        resp += 'username'
        resp += '<br>'
        resp += f"res['username'] != username"
        resp += '<br>'
        resp += res['username']
        resp += '<br>'
        resp += 'username'
        resp += '<br>'
        resp += f"{username}"
        resp += '<br>'  
        resp += '-' * 160
        resp += '<br>'
            
        resp += 'password'
        resp += '<br>'
        resp += f"res['password'] != password"
        resp += '<br>'
        resp += res['password']
        resp += '<br>'
        resp += 'password'
        resp += '<br>'
        resp += password
        # return f"No (´;ω;`)"
        return resp


if __name__ == "__main__":
    app.run(port=5000)


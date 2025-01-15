from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from dataclasses import dataclass
import os
from dotenv import load_dotenv

app = Flask(__name__)
app.secret_key = os.urandom(24)
load_dotenv()
PASSWORD = os.getenv("PASSWORD")
entries = []

# DB-URI config
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}".format(
    dbuser=os.environ.get("DBUSER", "default_user"),
    dbpass=os.environ.get('DBPASS', "default_pass"),
    dbhost=os.environ.get('DBHOST', "localhost"),
    dbname=os.environ.get('DBNAME', "default_db")
)

db = SQLAlchemy()
db.init_app(app)


@dataclass
class Entry:
    id: int
    content: str
    timestamp: datetime = datetime.now()


@app.route('/')
def index():
    return render_template('index.html', entries=entries)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_password = request.form.get('password')
        if user_password == PASSWORD:
            session['logged_in'] = True
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Incorrect password. Please try again.', 'error')
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logged out successfully.', 'success')
    return redirect(url_for('index'))


@app.route('/add_entry', methods=['POST'])
def add_entry():
    content = request.form.get('content')
    if content:
        entry_id = len(entries) + 1
        entry = Entry(id=entry_id, content=content)
        entries.append(entry)
    return redirect(url_for('index'))


@app.route('/delete_entry/<int:entry_id>', methods=['POST'])
def delete_entry(entry_id):
    global entries
    entries = [entry for entry in entries if entry.id != entry_id]
    flash('Entry deleted successfully!', 'success')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host="0.0.0.0")

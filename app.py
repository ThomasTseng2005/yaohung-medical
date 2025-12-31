from flask import Flask, render_template, redirect, url_for, request, session, send_from_directory
import os, sys
import time
from dotenv import load_dotenv

load_dotenv()  # 讀取 .env

app = Flask(__name__)

@app.context_processor
def inject_timestamp():
    return {'timestamp': int(time.time())}

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'ms-icon-310x310.png', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    return render_template("home.html", title="", navbar="trans", footer="0rem", footer_two="0rem")

@app.route('/about')
def about():
    return render_template("about.html", title="", navbar="green", footer="3rem", footer_two="3rem")

@app.route('/equipment')
def equipment():
    return render_template("equipment.html", title="", navbar="green", footer="3rem", footer_two="3rem")

@app.route('/appointment')
def appointment():
    return render_template("appointment.html", title="", navbar="green", footer="7.5rem", footer_two="7.5rem")

@app.route('/online-appointment')
def online_appointment():
    return render_template("online-appointment.html", title="", navbar="green", footer="7.5rem", footer_two="7.5rem")

@app.route('/events')
def events():
    return render_template("events.html", title="", navbar="green", footer="7.5rem", footer_two="7.5rem")

@app.route('/environment')
def environment():
    return render_template("environment.html", title="", navbar="green", footer="0", footer_two="0")

@app.route('/articles')
def articles():
    return render_template("articles.html", title="", navbar="green", footer="0", footer_two="0")

@app.route('/articles/<article>')
def article(article):
    return render_template(f"articles/{article}.html", title="", navbar="green", footer="0", footer_two="0")

@app.route('/contact')
def contact():
    return render_template("contact.html", title="", navbar="green", footer="2rem", footer_two="2rem")

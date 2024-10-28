from flask import Flask, render_template, redirect, url_for, request, session, send_from_directory
import os, sys
import smtplib, ssl
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'ms-icon-310x310.png', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def home():
    timestamp = int(time.time())
    return render_template("home.html", title="", navbar="trans", footer="0rem", footer_two="0rem", timestamp=timestamp)

@app.route('/about')
def about():
    return render_template("about.html", title="", navbar="green", footer="3rem", footer_two="3rem")

@app.route('/equipment')
def equipment():
    return render_template("equipment.html", title="", navbar="green", footer="3rem", footer_two="3rem")

@app.route('/events')
def events():

    return render_template("events.html", title="", navbar="green", footer="7.5rem", footer_two="7.5rem")

@app.route('/environment')
def environment():
    return render_template("environment.html", title="", navbar="green", footer="0", footer_two="0")

@app.route('/contact', methods=["GET", "POST"])
def contact():
    response = ""
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        subject = request.form["subject"]
        body = request.form["body"]
        to_email = "newmoking1129@gmail.com"
        to_email = "0830thomastseng@gmail.com"
        to_email_two = str(email)
        from_email = "yaohungclinic@gmail.com"
        username = "yaohungclinic@gmail.com"
        password = "clinic2020"
        main_message = 'Subject: {}\n\n{}'.format(subject, "From: " + str(name) + "\n\n" + "Email: " + str(
            email) + "\n\n" + "Phone: " + str(phone) + "\n\n" + "Body: \n" + str(body))
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email
        text = ""
        html = """
            <html>
                <head>
                    <meta charset="UTF-8">
                </head>
                <body style="">
                    <div style="padding: 1.3rem 0.7rem; background: rgb(191, 175, 141);">
                        <h1 style="color: white; margin: auto; width: 50%; text-align: center; font-weight: 300;">聯絡我們</h1>
                    </div>
                    <div style="padding: 2rem; background: #f0f0eb;">
                        <p style="color: black;">""" + name + """ 您好,</p>
                        <p style="color: black;">感謝您與我們聯絡！ 我們會盡快來回覆您的訊息。</p>
                        <p style="color: black;">如果您有更多的需要可以傳送 Email 到 <a href="mailto:yaohungclinic@gmail.com">yaohungclinic@gmail.com</a> 或撥打電話到 <a href="tel:+886 22984-0101">02-2984-0101</a>。 謝謝！</p>
                        <br>
                        <p style="color: black; font-weight: 500;">曜弘診所</p>
                    </div>
                </body>
            </html>
            """
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(from_email, to_email, main_message.encode('utf-8'))
            server.sendmail(from_email, to_email_two, msg.as_string())
            server.quit()
            response = "傳送成功！"
        except:
            response = "傳送失敗！"
    return render_template("contact.html", title="", navbar="green", footer="2rem", footer_two="2rem", response=response)


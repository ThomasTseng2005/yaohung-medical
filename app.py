from flask import Flask, render_template, redirect, url_for, request, session, send_from_directory
import os, sys
import requests
import smtplib, ssl
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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

@app.route('/contact', methods=["GET", "POST"])
def contact():
    response = ""
    if request.method == "POST":
        # Honeypot Verification
        if request.form.get("fax"):
            print("Honeypot triggered!")
            # Returen fake success to fool the bot
            return render_template("contact.html", title="", navbar="green", footer="2rem", footer_two="2rem", response="傳送成功！")

        # Turnstile Verification
        turnstile_response = request.form.get("cf-turnstile-response")
        turnstile_secret = os.getenv("TURNSTILE_SECRET_KEY")
        verify_url = os.getenv("VERIFY_URL", "https://challenges.cloudflare.com/turnstile/v0/siteverify")

        if turnstile_response and turnstile_secret:
            data = {
                "secret": turnstile_secret,
                "response": turnstile_response
            }
            try:
                verify_req = requests.post(verify_url, data=data)
                verify_res = verify_req.json()
                if not verify_res.get("success"):
                    return render_template("contact.html", title="", navbar="green", footer="2rem", footer_two="2rem", response="驗證失敗，請重試！")
            except Exception as e:
                print(f"Turnstile error: {e}")
                return render_template("contact.html", title="", navbar="green", footer="2rem", footer_two="2rem", response="驗證錯誤，請稍後再試！")
        else:
             return render_template("contact.html", title="", navbar="green", footer="2rem", footer_two="2rem", response="請完成驗證！")

        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        subject = request.form["subject"]
        body = request.form["body"]
        to_email = "yaohunggi@gmail.com"
        to_email_two = str(email)
        from_email = "曜弘診所-聯絡我們<yaohunggi@gmail.com>"
        username = os.getenv("MAIL_USERNAME", "").strip()
        password = os.getenv("MAIL_PASSWORD", "").strip()
        # print(f"Username: '[{username}]', Length: {len(username)}")
        # print(f"Password: '[{password}]', Length: {len(password)}")
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
        except Exception as e:
            response = "傳送失敗！"
            print("Email error:", e)
            
    return render_template("contact.html", title="", navbar="green", footer="2rem", footer_two="2rem", response=response)


from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)  # looks for index.html in same folder

# -------------------
# MAIL CONFIG
# -------------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'feroanmothy666@gmail.com'     # your email
app.config['MAIL_PASSWORD'] = 'feiu btxy jgzq sdzz'            # your Gmail App Password

mail = Mail(app)

# -------------------
# ROUTES
# -------------------
@app.route('/')
def index():
    return render_template('index.html')  # serves your existing index.html

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form.get('name')
    email = request.form.get('email')
    message_body = request.form.get('message')

    formatted_message = f"""Name: {name}
Contact: {email}

Message:
{message_body}"""

    msg = Message("New Contact Form Submission",
                  sender=app.config['MAIL_USERNAME'],
                  recipients=['feroanmothy666@gmail.com'])  # your email
    msg.body = formatted_message

    mail.send(msg)

    return "OK"

@app.route('/our-works')
def our_works():
    return render_template('our works.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blogs')
def blogs():
    return render_template('blog.html')

@app.route('/blog1')
def blog1():
    return render_template('blog pages/blog1.html')

@app.route('/blog2')
def blog2():
    return render_template('blog pages/blog2.html')

@app.route('/blog3')
def blog3():
    return render_template('blog pages/blog3.html')

@app.route('/blog4')
def blog4():
    return render_template('blog pages/blog4.html')

# -------------------
# MAIN
# -------------------
if __name__ == '__main__':
    app.run(debug=True)

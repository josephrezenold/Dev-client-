from flask import Flask, request, render_template
from twilio.rest import Client

app = Flask(__name__)

# -------------------
# TWILIO CONFIG
# -------------------
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
from_whatsapp_number = 'whatsapp:+918939843825'  # Twilio Sandbox number
to_whatsapp_number = 'whatsapp:+917358113731'   # Your verified WhatsApp number

client = Client(account_sid, auth_token)

# -------------------
# ROUTES
# -------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send-whatsapp', methods=['POST'])
def send_whatsapp():
    name = request.form.get('name')
    email = request.form.get('email')
    message_body = request.form.get('message')

    formatted_message = f"""New Contact Form Submission:

Name: {name}
Email: {email}
Message: {message_body}
"""

    message = client.messages.create(
        body=formatted_message,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )

    return "Message sent via WhatsApp"

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

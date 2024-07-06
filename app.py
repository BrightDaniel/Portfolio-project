from flask import Flask, render_template, request, redirect, url_for, flash
import os
from flask_mail import Mail, Message
from dotenv import load_dotenv


app = Flask(__name__)

# configurations for the session management
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# configure the email settings
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = os.getenv('MAIL_PORT')
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)






# routes

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # compose the email

        msg = Message("New Contact Form Submmision - Portfolio webiste",
                      sender=email,
                      recipients=[app.config['MAIL_DEFAULT_SENDER']])
        
        msg.body = f"Name: {name}\n\nEmail: {email}\n\nMessage:\n{message} "
        
        mail.send(msg)

        flash('Message sent successfully!', 'success')
        return redirect(url_for('home'))
    




if __name__ == '__main__':
    app.run(debug=True)
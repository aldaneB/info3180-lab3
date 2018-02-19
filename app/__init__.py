from flask import Flask
from flask_mail import Mail 



app = Flask(__name__)
app.config['SECRET_KEY'] = 'random'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = '40897a0fd0a2e3'
app.config['MAIL_PASSWORD'] = '27bc76d7150a7a'

mail = Mail(app)



from app import views
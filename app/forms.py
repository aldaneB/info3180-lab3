from flask_wtf import Form 
from wtforms.fields import TextField,TextAreaField
from wtforms import validators, ValidationError


class ContactForm(Form):
    name = TextField('Name', [validators.Required("(Required)")])
    email = TextField('Email',[validators.Required("(Required)")])
    subject = TextField('Subject',[validators.Required("(Required)")])
    message = TextAreaField('Message',[validators.Required("(Required)")])
    
    

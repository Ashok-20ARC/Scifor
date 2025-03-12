from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,FloatField
from wtforms.validators import DataRequired,Email,EqualTo

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=StringField('Password',validators=[DataRequired(),EqualTo('confirm',message='Passwords must match')])
    confirm=PasswordField('Confirm Password')
    submit=SubmitField('Register')

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=StringField('Password',validators=[DataRequired()])
    submit=StringField('Login')

class ProductForm(FlaskForm):
    name=StringField('Product Name',validators=[DataRequired()])
    price=FloatField('Price',validators=[DataRequired()])
    image=StringField('Image URL',validators=[DataRequired()])
    submit=SubmitField('Add Product')
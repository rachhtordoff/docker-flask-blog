from flask_wtf import Form
from wtforms import StringField, BooleanField, RadioField, DateTimeField, IntegerField, validators, TextField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class AccountsetupForm(Form):
    title = RadioField('Title', choices=[('mr', 'Mr'), ('miss', 'Miss'), ('mrs', 'Mrs'), ('ms', 'Ms')])
    firstname = StringField('FirstName', validators=[DataRequired()])
    lastname = StringField('LastName', validators=[DataRequired()])
    dob = DateTimeField('Date Of Birth', format='%d/%m/%y', validators=[DataRequired()])
    gender = RadioField('Gender', choices=[('female', 'Female'), ('male', 'Male')])
    email = TextField('Email Address', [validators.Length(min=6, max=35)])
    number = IntegerField('Contact No.', [validators.NumberRange(min=0, max=10)])

class AccountquestionairreForm(Form):
    question1 = RadioField('Do you often feel stressed and think there is something holding you back from a much more successful life?',  choices=[('true','Yes'),('false','No')])
    question2a = StringField('Out of 100 percent for both categories how much is stress and indecision in your life costing you in emotional and physical terms? ', validators=[DataRequired()])
    question2a =StringField('Out of 100 percent for both categories how much is stress and indecision in your life costing you in emotional and physical terms? ', validators=[DataRequired()])
    question3 = RadioField('Do you feel substantially more alive or further ahead than you did a year ago?',  choices=[('true','Yes'),('false','No')])
    question4 = RadioField('Do you often know what you ‘should’ be doing but have a difficult time actually doing it?',  choices=[('true','Yes'),('false','No')])
    question5 = RadioField(' If you have a career is it more of a job than a calling?',  choices=[('true','Yes'),('false','No')])
    question6 = RadioField(' Is there less meaning in your life, career, relationship or business than you would like?',  choices=[('true','Yes'),('false','No')])
    question7 = RadioField(' Do you have a difficult time balancing your career, family, friends, health, etc? ',  choices=[('true','Yes'),('false','No')])
    question8 = RadioField(' Do you often find yourself living automatically or just going through the motions?  ',  choices=[('true','Yes'),('false','No')])
    question9 = RadioField('Do you routinely find yourself worrying about the future? ',  choices=[('true','Yes'),('false','No')])
    question10 = RadioField('  Do you want more success, peace, close relationships or a sense that your life is making a difference?',  choices=[('true','Yes'),('false','No')])
    question11 = RadioField(' Do you ever get a sense that you are not living the life you were meant to live and that there is much more to life than you are now experiencing? ',  choices=[('true','Yes'),('false','No')])
    question12 = RadioField(' Do you have someone in your life who routinely gives you independent feedback and helps you to see what you might be missing? ',  choices=[('true','Yes'),('false','No')])

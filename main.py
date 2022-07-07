import flask
from flask import Flask, render_template
import os
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

year = datetime.today().year


@app.context_processor
def inject_year():
    return dict(year=year)


class ContactForm(FlaskForm):
    name = StringField(validators=[DataRequired(message="Please enter your name.")])
    email = EmailField(validators=[Email(message="Please enter your email.")])
    message = TextAreaField(validators=[DataRequired(message="A message is required")])
    submit = SubmitField()


@app.route('/', methods=["GET", "POST"])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        return " form not functional yet"
    print(flask.request.method)
    return render_template("index.html",form=form,method=flask.request.method)


if __name__ == "__main__":
    app.run(debug=True)

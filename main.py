from flask import Flask,render_template
import os
from datetime import datetime
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

year = datetime.today().year

@app.context_processor
def inject_year():
    return dict(year=year)

@app.route('/')
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

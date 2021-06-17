from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["CACHE_TYPE"] = "null"
app.static_folder = 'static'

@app.route('/')
def first_page():
    return render_template('index.html')
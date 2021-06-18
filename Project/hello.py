from flask import Flask
from flask import request
from flask import render_template
import os
from os.path import join, dirname, realpath

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["CACHE_TYPE"] = "null"
app.static_folder = 'static'
UPLOADS_PATH = "C:\\Users\\ADMIN\Desktop\\Swetha\\Academics\\Resume-Analyser-Software\\Project\\static"
app.config['UPLOAD_FOLDER'] = UPLOADS_PATH

@app.route('/')
def first_page():
    return render_template('index.html')

@app.route('/studentupload')
def student_page():
    return render_template('student.html')

@app.route('/recuriterupload')
def recuriter_page():
    return render_template('recruiter.html')

@app.route('/studentdashboard', methods=['GET', 'POST'])
def student_dashboard():
    if request.method=='POST':
        print("HI")
        f = request.files['resume']
        print(f)
        f.save(os.path.join(UPLOADS_PATH,f.filename))
        original_filename = f.filename
        path = "C:\\Users\\ADMIN\Desktop\\Swetha\\Academics\\Resume-Analyser-Software\\Project\\static"+f.filename
        return "Hi"

@app.route('/recuriterdashboard', methods=['GET', 'POST'])
def recuriter_dashboard():
    if request.method=='POST':
        print("HI")
        files = request.files.getlist('resume')
        print(files)
        for f in files:
            print(f)
            f.save(f.filename)
            original_filename = f.filename
            path = "C:\\Users\\ADMIN\Desktop\\Swetha\\Academics\\Resume-Analyser-Software\\Project\\static"+f.filename
        return "Hi"
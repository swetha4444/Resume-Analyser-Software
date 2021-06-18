from flask import Flask
from flask import request
from flask import render_template
import os
import pandas as pd
from os.path import join, dirname, realpath
from parseResume import *
import execute
from execute import execute_main


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
        f.save(f.filename)
        # Rename the file as resume and replace it .
        original = f.filename
        output = 'resume.docx'
        try:
            os.rename(original, output)
        except WindowsError:
            os.remove(output)
            os.rename(original, output)
        docxToCsv("resume.docx")
        execute_main()
        resume_df = pd.read_csv('data.csv')
        return render_template("studentSummary.html", row_data=list(resume_df.values.tolist()), zip=zip)

@app.route('/studentSummary')
def student_summary():
    resume_df = pd.read_csv('data.csv')
    return render_template('studentSummary.html', tables=[resume_df.to_html(classes='data')])

@app.route('/studentGraph')
def student_Graph():
    return render_template('studentGraph.html')

@app.route('/studentJob')
def student_Job():
    return render_template('studentJob.html')

@app.route('/recuriterdashboard', methods=['GET', 'POST'])
def recuriter_dashboard():
    if request.method=='POST':
        print("HI")
        files = request.files.getlist('resume')
        print(files)
        for f in files:
            print(f)
            f.save(f.filename)
        return "Hi"
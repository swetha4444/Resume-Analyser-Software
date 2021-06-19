from flask import Flask
from flask import request
from flask import render_template
import os
import pandas as pd
from os.path import join, dirname, realpath
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split

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
    return render_template('studentSummary.html', row_data=list(resume_df.values.tolist()), zip=zip)

@app.route('/studentGraph')
def student_Graph():
    return render_template('studentGraph.html')

@app.route('/studentJob')
def student_Job():
    resume_df = pd.read_csv('summary_data.csv')
    user_text = resume_df.workExp[len(resume_df)-1]
    print(user_text)
    # Encode the text
    encoded_docs = [one_hot(user_text, 500)]
    # pad documents to a max length
    padded_text = pad_sequences(encoded_docs, maxlen=500, padding='post')
    model = load_model("model.h5")
    # Prediction based on model
    prediction = model.predict(padded_text)
    # Decode the prediction
    encoder = LabelBinarizer()
    data = pd.read_csv('Cleaned_JobDescs.csv', header = 0, names = ['Query', 'Description'])
    train, test = train_test_split(data, test_size = 0.1, random_state = 17) #random_state = None
    test_labels = test['Query']
    encoder.fit(test_labels)
    result = encoder.inverse_transform(prediction)
    print(result)
    return render_template('studentJob.html', job=result[0])

@app.route('/recuriterdashboard', methods=['GET', 'POST'])
def recuriter_dashboard():
    if request.method=='POST':
        print("HI")
        files = request.files.getlist('resume')
        print(files)
        for f in files:
            print(f)
            f.save(f.filename)
        FolderOfDocxToCSV('./Resumes')
        execute_main()
        resume_df = pd.read_csv('summary_data.csv')
        resume_df = resume_df.drop(['workExp','about'],axis=1)
        return render_template("recruiterSummary.html", tables=[resume_df.to_html(classes='data steelBlueCols',table_id="myTable", header="true")])
    
@app.route('/recruiterSummary')
def recruiter_summary():
    resume_df = pd.read_csv('summary_data.csv')
    resume_df = resume_df.drop(['workExp','about'],axis=1)
    return render_template('recruiterSummary.html', tables=[resume_df.to_html(classes='table-dark',table_id="myTable", header="true")])

@app.route('/recruiterGraph')
def recruiter_Graph():
    return render_template('recruiterGraph.html')

@app.route('/recruiterJob')
def recruiter_Job():
    freq = extract_freq_skills()
    print(freq)
    return render_template('recruiterJob.html', skills_freq = freq)
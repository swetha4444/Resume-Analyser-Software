from flask import Flask,request,render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["CACHE_TYPE"] = "null"
app.static_folder = 'static'

@app.route("/home")
def render_homepage() :
    return render_template("index.html")
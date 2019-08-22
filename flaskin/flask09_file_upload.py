#!/usr/bin/python3
import os
from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "./uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/uploader", methods = ["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files['file']
        #f.save(secure_filename(f.filename))
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
        return "file uploaded successfull!"

if __name__ == "__main__":
    app.run(port=5006)



from flask import Flask, render_template, send_file ,request, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'C:\\Users\\rohan.mehta\\PycharmProjects\\ResumeUpload\\static\\txt\\'


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/download')
def download_file():
    path = 'C:\\Users\\rohan.mehta\\PycharmProjects\\ResumeUpload\\data.txt'
    return send_file(path,as_attachment=True)

@app.route('/upload')
def upload_file():
    return render_template('upload.html')


if __name__ == "__main__":
    app.run(debug=True)
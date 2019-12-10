from flask import Flask, render_template, send_file ,request, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/download')
def download_file():
    path = '\data.txt'
    return send_file(path,as_attachment=True)

#https://stackoverflow.com/questions/39801728/using-flask-to-load-a-txt-file-through-the-browser-and-access-its-data-for-proce

@app.route('/upload')
def upload_file():
    if request.method == 'POST':
        return "PoSTed"
        # f = request.files['uploadedtxt']
        # f.save(secure_filename(f.filename))
        # return 'file uploaded successfully'


if __name__=="__main__":
    app.run(debug=True)
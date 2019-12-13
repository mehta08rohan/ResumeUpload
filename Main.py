from flask import Flask, render_template, send_file ,request, flash
from werkzeug.utils import secure_filename
import os
import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'C:\\Users\\rohan.mehta\\PycharmProjects\\ResumeUpload\\static\\txt\\'


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/download')
def download_file():
    path = 'C:\\Users\\rohan.mehta\\PycharmProjects\\ResumeUpload\\data.txt'
    return send_file(path,as_attachment=True)

@app.route('/upload', methods=['GET','POST'])
def upload_file():
    if request.method == "POST":
        f = request.files['file']
        # f.save(secure_filename(f.filename))
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        filename = f.filename.rsplit('.')
        date = str(datetime.datetime.now())
        date = date.replace('-', '').replace(':', '').replace('.', '').replace(' ','_')
        filename = filename[0] + date + '.' + filename[1]
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename)))

        with open(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(filename)),'r') as my_file:
            lines = my_file.readlines()
            my_list =[]
            for i in lines:
                my_list.append(i)
            return str(my_list)

        return render_template('my_form.html')
    return render_template('upload.html')


if __name__ == "__main__":
    app.run(debug=True)
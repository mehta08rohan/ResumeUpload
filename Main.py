from flask import Flask, render_template, send_file ,request, flash

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/download')
def download_file():
    path = '\data.txt'
    return send_file(path,as_attachment=True)



#https://stackoverflow.com/questions/39801728/using-flask-to-load-a-txt-file-through-the-browser-and-access-its-data-for-proce



if __name__=="__main__":
    app.run(debug=True)
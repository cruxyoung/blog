from flask import Flask
from flask import render_template, url_for,request

from subprocess import call




app = Flask(__name__)


@app.route('/base_test')
def base_test_page():
    return render_template('base.html')


@app.route('/')
def extend():
    return render_template('index.html')

@app.route('/download',methods=['GET','POST'])
def download_page():
    if request.method == 'POST':
        download_url = request.form.get('address','')
        # command = "youtube-dl -ict " + download_url
        command = "you-get " + download_url
        call(command.split(), shell=False)
        command = ""
    return render_template('download.html')

if __name__ == '__main__':
    app.run(debug=True )

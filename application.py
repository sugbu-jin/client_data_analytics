from flask import Flask, render_template, request, redirect, url_for
from flask import send_file
import os
from os.path import join, dirname, realpath

from data_converter import DataConverter

application = Flask(__name__)

# enable debugging mode
application.config["DEBUG"] = True

# Upload folder
UPLOAD_FOLDER = 'data'
application.config['UPLOAD_FOLDER'] =  UPLOAD_FOLDER

jsonData = ''

# Root URL
@application.route('/')
def index():
     # Set The upload HTML template '\templates\index.html'
    return render_template('index.html')


# Get the uploaded files
@application.route("/", methods=['POST'])
def uploadFiles():
    global jsonData

    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        file_path = os.path.join(application.config['UPLOAD_FOLDER'], uploaded_file.filename)

        # Set the file path
        uploaded_file.save(file_path)

        # Execute csv to json conversion
        jsonData = DataConverter().convert_csv2json(filepath=file_path)

    return render_template('content.html', text = jsonData)


@application.route('/download')
def downloadFile ():
    filepath = 'data/jsonData.txt'
    global jsonData

    with open (filepath, 'a') as f:
        f.write(jsonData)

    return send_file(filepath, as_attachment=True)


if (__name__ == "__main__"):
    try:
        application.run(port = 5000)
    except Exception as e:
        print ("Error: CSV file could not be found or invalid")

        usage = """
HOW TO RUN APPLICATION

OPTION 1: Run via Linux Terminal (for advanced users):
1. Open terminal and type:
        /usr/bin/python data_converter.py <path_to_csv_file>

        Ex:
        python data_converter.py 'data/data.csv'

OPTION 2: Run via Flask without Docker
1. Open terminal and type:
        python application.py
2. Open browser and access 'http://127.0.0.1:5000/'

OPTION 3: Run via Flask WITH Docker
1. Open terminal and type:
        'docker build –t <image_name> .'
        Example:
        docker build –t app_flask .
2. Verify if exists, type
        docker image ls
3. And then, run docker
        docker run  –p 5000:5000 <image_name>:advanced

OPTION 4: A sample Flask application is running, open any browser and type:
For sample running flask application, see:
        http://semilla-env.eba-n2kgtimw.us-east-1.elasticbeanstalk.com/

        """
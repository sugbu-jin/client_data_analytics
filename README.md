# data_converter
data_converter.py is a basic tool that processes custom client csv files and converts them to json format

Runs:
- Windows
- Linux

Requires:
- python3.xx installation
- pandas module
- flask module

Optional
- jupyter notebook (jupyterlab) - for easier viewing of pandas operations

Installation:
1. Install Python3
2. Open Linux terminal
3. Execute 'pip install -r requirements.txt'

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


Why pandas?
Pandas is an open source library in Python. It provides ready to use high-performance data structures and data analysis tools. Pandas module runs on top of NumPy and it is popularly used for data science and data analytics. It also provides streamlined alignment of tabular data and powerful time series functionality.

Why flask?
Flask is a lightweight web application framework based in Python. It is designed to make web applications quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks among developers.
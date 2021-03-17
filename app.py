from flask import Flask, request, render_template
import boto3

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')



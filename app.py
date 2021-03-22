from flask import Flask, request, render_template
import  s3_test, rds_test, ec2_test
import json

app = Flask(__name__)


@app.route('/ec2', methods=['POST'])
def create_ec2():
    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        response = ec2_test.create_ec2(data)
        return {"status": "working", "response":response}


@app.route('/s3', methods=['POST'])
def create_s3():
    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        response = s3_test.create_s3(data)
        return {"status": "working", "response": response}


@app.route('/rds', methods=['POST'])
def create_rds():
    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        response = rds_test.create_rds(data)
        return {"status": "working", "response": response}

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

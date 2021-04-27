from flask import Flask, request, render_template, send_file
import s3_test, rds_test, ec2_test
import json
import terraform_generator_for_S3, terraform_generator_for_EC2, terraform_generator_for_RDS


app = Flask(__name__)


@app.route('/ec2', methods=['POST'])
def create_ec2():
    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        response = ec2_test.create_ec2(data)
        terraform_generator_for_EC2.terraform_ec2(data)
        return {"status": "working", "response": response}


@app.route('/s3', methods=['POST'])
def create_s3():
    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        response = s3_test.create_s3(data)
        
        terraform_generator_for_S3.terraform_s3(data)
        return {"status": "working", "response": response}


@app.route('/rds', methods=['POST'])
def create_rds():
    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        response = rds_test.create_rds(data)
        terraform_generator_for_RDS.terraform_rds(data)
        return {"status": "working", "response": response}

@app.route('/download')
def download_file():
    print("here")
    path = '/home/aritra/PycharmProjects/aws_instance_generator/terraform/config.tf.json'
    return send_file(path, attachment_filename='config.tf.json',as_attachment=True)

@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True, port=8080, debug=True)

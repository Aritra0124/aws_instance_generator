from flask import Flask, request, render_template, jsonify
from flask.wrappers import Response
import random, json
import db

app = Flask(__name__)

def dbOP(data):
    database = db.database()
    database.connectDB('localhost', 'pmauser', 'aritraroot', 'aih')
    id = database.insertDetailsDB(data['name'], data['age'], data['gender'])
    database.disconnectDB()
    return int(id)

def healthOp(data):
    database = db.database()
    database.connectDB('localhost', 'pmauser', 'aritraroot', 'aih')
    id = database.insertHealthDB(data['id'], data['spo2'], data['heart_rate'], 0)
    database.disconnectDB()

@app.route('/save_user_health_data', methods=['POST'])
def save_data():
    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        print(data)
        healthOp(data)
        response = "working"
        return {"status": "1", "response": response}

@app.route('/save_user_data', methods=['POST'])
def save():
    if request.method == 'POST':
        data = json.loads(request.get_data(as_text=True))
        print(data)
        id = dbOP(data)
        response = "working"
        return {"status": id, "response": response}
        



@app.route('/')
def hello_world():
    return render_template('view.html')


if __name__ == '__main__':
    app.run( host ='0.0.0.0' ,threaded=True, port=8080, debug=True)

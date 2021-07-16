from flask import Flask, request, render_template, send_file
import json
import pymysql

app = Flask(__name__)

def db():
    db = pymysql.connect("localhost", "pmauser", "aritraroot", "tracker")
    cursor = db.cursor()
    sql = "select TIMEDIFF(%s, %s)"
    cursor.execute(sql, (data["to_time"], data["from_time"]))
    total_time = cursor.fetchone()
    sql = "insert into activity_update values(0,%s, %s, NOW(), %s, %s, %s)"
    id = cursor.execute(sql, (
        session["activity_id"], session['id'], data["from_time"], data["to_time"],
        total_time))
    db.commit()
    db.close()
    # id = cursor.fetchone()
    return id


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True, port=8080, debug=True)

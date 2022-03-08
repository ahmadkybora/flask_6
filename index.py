from flask import Flask, jsonify, render_template, request
import pymysql
from app import app
from db import mysql
from User import User
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

user = User()
@app.route("/")
def index():
    return user.getAllUser()
        # conn = None
        # cursor = None
        # try:
        #     conn = mysql.connect()
        #     cursor = conn.cursor(pymysql.cursors.DictCursor)
        #     cursor.execute("SELECT * FROM users")
        #     rows = cursor.fetchall()
        #     resp = jsonify(rows)
        #     resp.status_code = 200
        #     return resp
        # except Exception as e:
        #     print(e)
        # finally:
        #     cursor.close() 
        #     conn.close()

@app.route("/user")
def createUser():
    return render_template("index.html")

@app.route("/user/store", methods=['POST'])
def storeUser():
    username = request.form['username']
    email = request.form['email']
    return user.insertUser(username, email)
    # return email

if __name__ == "__main__":
    app.run(debug=True)

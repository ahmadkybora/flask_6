import pymysql
from flask import jsonify, redirect
from db import mysql

class User:
    # def __init__(self) -> None:
    #     pass
    conn = None
    cursor = None
    def getAllUser(self):
        # a = "hello"
        # return a
        # resp = jsonify("hello")
        # return resp
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM users")
            rows = cursor.fetchall()
            resp = jsonify(rows)
            resp.status_code = 200
            return resp
        except Exception as e:
            print(e)
        finally:
            cursor.close() 
            conn.close()

    def insertUser(self, username, email):
        try:
            conn = mysql.connect()
            # cursor = conn.cursor(pymysql.cursors.DictCursor)
            # insertSql = """"INSERT INTO users (username, email) VALUES (%s, %s)"""
            cursor = mysql.connect().cursor()
            cursor.execute("INSERT INTO users (username, email) VALUES ('" + username + "', '" + email + "')")
            cursor.connection.commit()
            # rec = (username, email)
            # cursor.execute(insertSql, rec)
            # rows = cursor.fetchall()
            # resp = jsonify(rows)
            # resp.status_code = 200
            # return resp
            return redirect("/")
        except Exception as e:
            print(e)
        finally:
            cursor.close() 
            conn.close()

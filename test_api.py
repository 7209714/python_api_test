import pandas as pd
import flask
from flask import jsonify
from time import sleep
from db_config import mysql
import pymysql
from db_config import mysql
from flask import flash, request
from werkzeug import generate_password_hash, check_password_hash

app = flask.Flask(__name__)

@app.route('/add', methods=['POST'])
def add_user():
    try:
        _json = request.json
        _name = _json['user_name']
        _studentID = _json['user_stuid']
#        _password = _json['pwd']
        # validate the received values
        if _name and _studentID and request.method == 'POST'  :
            #do not save password as a plain text
#            _hashed_password = generate_password_hash(_password)
            # save edits
            sql = "INSERT INTO apiuser(user_name, user_stuid) VALUES(%s, %s)"
            data = (_name, _studentID)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User added successfully!')
#            resp.status_code = 200
            cursor.close() 
            conn.close()
            return resp
        

        else:
            return not_found()
    except Exception as e:
        print(e)

'''
@app.route('/add/<string:name>/<string:student_ID>', methods=['GET'])
def add_user(mysqldb, cursor,name,student_ID):
    try:
#        _json = request.json
#        _name = _json['name']
#        _student_ID = _json['student_ID']
#        _password = _json['pwd']
        # validate the received values
        if name and student_ID  :
            #do not save password as a plain text
#            _hashed_password = generate_password_hash(_password)
            # save edits
            sql = "INSERT INTO user(name, student_ID) VALUES(%s, %s)"
            data = (name, student_ID)


            cursor.execute(sql, data)
            mysqldb.commit()
            resp = 'User added successfully!'
#            resp.status_code = 200
            return "<h1>successfully</h1>"
#        else:
#            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        mysqldb.close()
'''        


@app.route('/users')
def users():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM apiuser")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
      
@app.route('/user/<int:id>')
def user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM apiuser WHERE user_id=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
        
        

@app.route('/update', methods=['POST'])
def update_user():
    try:
        _json = request.json
        _id = _json['user_id']
        _name = _json['user_name']
        _stuid = _json['user_stuid']
        
        # validate the received values
        if _name and _stuid  and _id and request.method == 'POST':
            #do not save password as a plain text
#            _hashed_password = generate_password_hash(_password)
            # save edits
            sql = "UPDATE apiuser SET user_name=%s, user_stuid=%s WHERE user_id=%s"
            data = (_name, _stuid, _id)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User updated successfully!')
 #           resp.status_code = 200
            cursor.close() 
            conn.close()
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)


  
@app.route('/delete/<int:id>')
def delete_user(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM apiuser WHERE user_id=%s", (id,))
        conn.commit()
        resp = jsonify('User deleted successfully!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()
@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp
        

if __name__ == "__main__":
    app.run(debug=True)

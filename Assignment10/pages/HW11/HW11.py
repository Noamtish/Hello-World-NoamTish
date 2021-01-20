from flask import Blueprint, render_template
from flask import Flask,redirect,url_for,request,session
import mysql.connector
from flask import jsonify
from Assignment10.utilities.db.db_manager import  dbManager

# HW11 blueprint definition
HW11 = Blueprint('HW11', __name__, static_folder='static', static_url_path='/HW11', template_folder='templates')


# Routes
@HW11.route('/assignment11/users')
def all_users():
    if request.method == 'GET':
        query = "select * from users2"
        query_result = dbManager.fetch(query)
        data=jsonify({ 'success': 'True',   'Data': query_result}  )
    return data

@HW11.route('/assignment11/users/selected' ,defaults ={'user_id':3})
@HW11.route('/assignment11/users/selected/<int:user_id>')
def find_user(user_id):
    if request.method == 'GET':
        query = "select * from users2 where user_id=('%s')" % (user_id)
        query_result = dbManager.fetch(query)
    if len(query_result) == 0:

        return jsonify({
            "User": " Not exists",
            'success': 'False',
            'Data': [],

        })
    else:
        return jsonify({
            'success': 'True',
            'Data': query_result[0]
        })
    return render_template('Assignment11.html')



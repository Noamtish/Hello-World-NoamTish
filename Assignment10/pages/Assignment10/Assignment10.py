from flask import Blueprint, render_template
from flask import Flask,redirect,url_for,request,session
import mysql.connector
from utilities.db.db_manager import  dbManager

# Assignment10 blueprint definition
Assignment10 = Blueprint('Assignment10', __name__, static_folder='static', static_url_path='/Assignment10', template_folder='templates')


# Routes
@Assignment10.route('/Assignment10',methods=['post','get'])
def index():

    query1="select username,job from users"
    users=dbManager.fetch(query1)
    if(request.method =='GET'):
        query="select username,job from users"
        users= dbManager.fetch(query)





    return render_template('Assignment10.html',request_method=request.method,users=users)

@Assignment10.route('/Assignment10_insert',methods=['post','get'])
def insertuser():




    if (request.method == 'POST'):
        username=request.form['username']
        job=request.form['job']
        password=request.form['password']
        query = "insert into users(username,job,password) values ('%s','%s','%s')" %(username,job,password)
        print (query)
        dbManager.commit(query)
        session['action']= "insert"
    return redirect('/Assignment10')

@Assignment10.route('/Assignment10_update',methods=['post','get'])
def updateUser():
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        job = request.form['job']
        query = "update users  set job = ('%s') , password = ('%s') where  username = ('%s') "% (job, password,username)
        print(query)
        dbManager.commit(query)
        session['action'] = "update"
    return redirect('/Assignment10')


@Assignment10.route('/Assignment10_delete', methods=['post', 'get'])
def deleteUser():
    if (request.method == 'GET'):
        username = request.args['username']

        query = "delete from users where username = ('%s')" % (username)
        print(query)
        dbManager.commit(query)
        session['action'] = "delete"
    return redirect('/Assignment10')
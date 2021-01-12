from flask import Flask, render_template,redirect,url_for,request,session
import mysql.connector
app=Flask(__name__)
app.secret_key = 'session126'



# def interact_db(query,query_type: str):
#     return_value=False
#     connection =mysql.connector.connect(host='localhost',
#                                         user='root',password='poipbnm789',database='web_class')
#     cursor=connection.cursor(named_tuple=True) #allow you to use .id
#     cursor.excute(query)
#
#     if query_type == 'commit':
#         #when use insert update delete statement
#         connection.commit()
#         return_value=True
#
#     if query_type == 'commit':
#         # when use insert update delete statement
#         query_result=cursor.fetchall()
#         return_value = query_result
#
#     connection.close()
#     cursor.close()
#     return  return_value
#
#
#
#
#



@app.route('/')
def Home():
    session['username']= ''
    return 'Home Page'

@app.route('/page1')
def CV():
    return render_template('final_cv.html')

@app.route('/Contact')
def change_loc():
    return render_template('contact.html')


@app.route('/Assignment8')
def A8():
    return render_template('Assignment8.html', name='Noam', dogs=['tokyo', 'shibel', 'rio'])


@app.route('/Assignment9_logout',methods=['post','get'])
def logout():
    session['logged_in'] = False
    username = ''
    session['username']=username
    return redirect(url_for('A9'))


@app.route('/Assignment9',methods=['post','get'])
def A9():
  User_List={"noam": "student", "tomer": "mailmen", "sharon": "teacher", "amit": "Soccer player"}
  name = 'empty'

  #session['logged_in'] = False

  if request.method == 'GET':

    if 'name' in request.args:

        name = request.args['name']

  if request.method == 'POST':

    username = request.form['username']
    session['username'] = username
    session['logged_in'] = True




  return render_template('Assignment9.html', R_method=request.method, name=name, User_List=User_List,username=session['username'])





@app.route('/temp2')
def temp2():
    return render_template('temp2.html', name='Noam',cats=['mizi', 'maizil', 'garfild'])




#redirect by the name of the func
@app.route('/nic')
def call_func():
    return redirect(url_for('hello'))
@app.route('/hello')
def hello():
    return 'hweloooo'






if __name__== '__main__':
    app.run(debug=True)
from flask import Flask, render_template,redirect,url_for,send_file

app=Flask(__name__)
@app.route('/')
@app.route('/page1')
def home():
    return render_template('final_cv.html')

@app.route('/Contact')
def change_loc():
    return render_template('contact.html')


@app.route('/Assignment8')
def A8():
    return render_template('Assignment8.html', name='Noam', dogs=['tokyo', 'shibel', 'rio'])

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
from flask import Flask,render_template,request
from BookStore import app
from BookStore.models import User,Books,Person
from BookStore.database import db_session
import time

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/test')
def Test():
    return render_template('test.html')



@app.route('/login')
def Login():
    return render_template('login.html')    


@app.route('/loginpost',methods = ['POST','GET'])
def loginpost():
    return render_template('test.html')


@app.route('/registerpost',methods = ['POST','GET'])
def registerpost():
    if request.method == 'POST':
        username = request.form['user_number']
        password = request.form['password']
        if not username is None and not password is None:
            new_user = User(username, password)
            db_session.add(new_user)
            db_session.commit()
    time.sleep(2)
    return render_template('index.html')  



@app.route('/register')
def Register():
    return render_template('register.html')

@app.route('/personal')
def Personal():
    return render_template('personal.html')


@app.route('/user_namepost',methods = ['POST','GET'])
def user_namepost():
    if request.method == 'POST':
        user_number = request.form['user_number']
        name = User.query.filter_by(username = user_number).first()
        if name:
            return "1"
        else:
            return user_number


@app.route('/cmp_pwd', methods = ['POST','GET'])
def Cmp_Pwd():
    if request.method == 'POST':
        user_name = request.form['username']
        user = User.query.filter_by(username = user_name).first()
        if user.password == request.form['password']:
            return "1"
        else:
            return "0"
        return render_template('index.html')
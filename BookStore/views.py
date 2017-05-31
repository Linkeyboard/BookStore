from flask import Flask,render_template,request,session, redirect
from BookStore import app
from BookStore.models import User,Books,Person
from BookStore.database import db_session
import time

@app.route('/')
def Index():
    print(session)
    if 'Username' in session:
        Have_logged = True
    else:
        Have_logged = False
    return render_template('index.html',Have_logged = Have_logged)

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
        print(username,password)
        if not username is None and not password is None:
            new_user = User(username, password)
            db_session.add(new_user)
            db_session.commit()
            session['Username'] = username
            print("register",username)
    time.sleep(2)
    print(session,1)
    return redirect('/')



@app.route('/register')
def Register():
    return render_template('register.html')

@app.route('/login_get')
def login_get():
    return redirect('/')

@app.route('/personal')
def Personal():
    return render_template('personal.html')


@app.route('/user_namepost',methods = ['POST','GET'])
def user_namepost():
    if request.method == 'POST':
        user_number = request.form['user_number']
        name = User.query.filter_by(username = user_number).first()
        if name:
            session['Username'] = user_number
            return "1"
        else:
            return user_number


@app.route('/cmp_pwd', methods = ['POST','GET'])
def cmp_pwd():
    if request.method == 'POST':
        user_name = request.form['user_number']
        user = User.query.filter_by(username = user_name).first()
        session['Username'] = user_name
        if user.password == request.form['pwd']:
            return "1"
        else:
            return "0"


@app.route('/sleep', methods = ['POST','GET'])
def Sleep():
    time.sleep(1)
    return "1"


@app.route('/addperson', methods = ['POST','GET'])
def addperson():
    real_name = request.form['real_name']
    address = request.form['address']
    phone = request.form['phone']
    user_id = request.form['user_id']
    if 'Username' not in session:
        session['Username'] = 'Air'
    U_name = session['Username']
    p = Person(user_id , real_name , address , phone , U_name)
    db_session.add(p)
    db_session.commit()
    return redirect('/')



@app.route('/homeotherbook')
def home_otherbook():
    return render_template('home_otherbook.html')

@app.route('/hometeachbook')
def home_teachbook():
    return render_template('home_teachbook.html', Session = session )


@app.route('/hometoolbook')
def home_toolbook():
    return render_template('home_toolbook.html', Session = session )
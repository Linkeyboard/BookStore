from flask import Flask,render_template,request,session, redirect, url_for
from BookStore import app
from BookStore.models import User,Books,Person,BookState
from BookStore.database import db_session
import time
from werkzeug.utils import secure_filename
import os
import json

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
    return redirect('/hometoolbook')



@app.route('/homeotherbook')
def home_otherbook():
    b = Books.query.filter_by( kind = "其他").all()
    ll = len(b)
    return render_template('home_otherbook.html', Session = session,s_book = b, ll = len(b) )

@app.route('/hometeachbook')
def home_teachbook():
    b = Books.query.filter_by( kind = "教科书").all()
    ll = len(b)
    return render_template('home_teachbook.html', Session = session,s_book = b, ll = len(b) )


@app.route('/hometoolbook')
def home_toolbook():
    b = Books.query.filter_by( kind = "工具书").all()
    ll = len(b)
    return render_template('home_toolbook.html', Session = session, s_book = b, ll = len(b) )


@app.route('/soldbook')
def soldbook():
    b = Books.query.filter_by( owner=session['Username'] ).all()
    print(len(b))
    return render_template('soldbook.html', Session = session , s_book = b , ll = len(b))

@app.route('/deletebook',methods=['POST'])
def deletebook():
    b = Books.query.filter_by( owner=session['Username'] ,name=request.form['book_name']).first()
   # bb = Books(b.name, b.author,b.price,b.intro,b.kind,b.path,b.owner)
    db_session.delete(b)
    db_session.commit()
    return redirect('/soldbook')


@app.route('/deletebook2',methods=['POST'])
def deletebook2():
    b = Books.query.filter_by(name=request.form['book_name']).first()
    print('test',request.form['book_name'],b)
    bb = BookState.query.filter_by(bookid = b.id).first()
    db_session.delete(bb)
    db_session.commit()
   # bb = Books(b.name, b.author,b.price,b.intro,b.kind,b.path,b.owner)
    #db_session.delete(b)
    ##db_session.commit()
    return redirect('/collectbook')

UPLOAD_FOLDER = 'BookStore/static/Uploads'

@app.route('/upload', methods=['GET', 'POST'])

def upload():
    if request.method == 'POST':
        f = request.files['file']
        fname = secure_filename(f.filename) #获取一个安全的文件名，且仅仅支持ascii字符；
        print(fname)
        f.save(os.path.join(UPLOAD_FOLDER, fname))
        book_name = request.form['book_name']
        author = request.form['author']
        intro = request.form['intro']
        price = request.form['price']
        kind = request.form['kind']
        b = Books(book_name,author,price,intro,kind,fname,session['Username'])
        db_session.add(b)
        db_session.commit()
    return redirect('/soldbook')



@app.route('/purchasedbook')
def purchasedbook():
    bb = BookState.query.filter_by(bookselector = session['Username'],bookstate = 2).all()
    b=[]
    for i in bb:
        if Books.query.filter_by(id = i.bookid).first():
            b.append(Books.query.filter_by(id = i.bookid).first())
    print("purchase",b)
    return render_template('purchasedbook.html', Session = session, s_book = b, ll = len(b) )


@app.route('/collectbook')
def collectbook():
    bb = BookState.query.filter_by(bookselector = session['Username'],bookstate = 1).all()
    b=[]
    for i in bb:
        if Books.query.filter_by(id = i.bookid).first():
            b.append(Books.query.filter_by(id = i.bookid).first())
    print(b)
    return render_template('collectbook.html', Session = session, s_book = b, ll = len(b) )



@app.route('/bookDetail/<bookid>')
def bookDetail(bookid):
    print('Bookdetail',bookid)
    b = Books.query.filter_by(id = bookid).first()
    return render_template('bookDetail.html', Session = session,s_book = b)


@app.route('/searchbook')
def searchbook():
    return render_template('searchbook.html', Session = session )


@app.route('/shoucangbook',methods=['POST'])
def shoucangbook():
    print(request.form['book_id'])
    bs = BookState(request.form['book_id'],session['Username'],1)
    db_session.add(bs)
    db_session.commit()
    return redirect('/collectbook')


@app.route('/have_information',methods=['POST','GET'])
def hava_information():
    if request.method == 'POST':
        p = Person.query.filter_by(username=session['Username']).first()
        print("information",request.form['bookname'])
        p_ = Books.query.filter_by(name = request.form['bookname']).first()
        if not p:
            return ""
        else:
            pp={}
            pp['id'] = p.id
            pp['name'] = p.name
            pp['phone'] = p.phone
            pp['address'] = p.address
            pp['username'] = session['Username']
            pp['price'] = p_.price
            pp['bookNAME'] = p_.name
            return json.dumps(pp)
    else:
        return redirect('/')


@app.route('/add_buy',methods = ['POST','GET'])
def add_buy():
    if request.method == 'POST':
        b = Books.query.filter_by(name=request.form['bookname']).first()
        if b:
            bk = BookState(b.id,session['Username'],2)
            db_session.add(bk)
            db_session.commit()

    return redirect('/hometoolbook')

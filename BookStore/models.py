from sqlalchemy import Column, Integer, String
from BookStore.database import Base

class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(200),nullable = False)
    author = Column(String(200))
    price = Column(String(200))
    intro = Column(String(1000))
    kind = Column(String(100))
    path = Column(String(100))
    owner = Column(String(200))

    def __init__(self, name=None, author=None,price = None,intro = None,kind=None,path = None,owner = None):
        self.name = name
        self.author = author
        self.price = price
        self.intro = intro
        self.kind = kind
        self.path = path
        self.owner = owner
        

    def __repr__(self):
        return '<Book: %r>' % (self.name)



class Person(Base):
    __tablename__ = 'person'
    id = Column(String(100), primary_key=True)
    name = Column(String(200) ,nullable = False)
    phone = Column(String(200),nullable = False)
    address = Column(String(2000))
    username = Column(String(200))

    def __init__(self,id=None, name=None, phone=None,address=None,username = None):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
        self.username = username
        
    def __repr__(self):
        return '<id:%r name:%r>' % (self.id,self.name)


class User(Base):
    __tablename__ = 'user'
    username = Column(String(200) ,nullable = False, primary_key=True)
    password = Column(String(200),nullable = False)

    def __init__(self,username=None, password=None):
        self.username = username
        self.password = password


    def __repr__(self):
        return '<username:%r>' % (self.username)



class BookState(Base):
    __tablename__ = 'bookstate'
    bookid = Column(Integer ,nullable = False, primary_key=True)
    bookselector = Column(String(200),nullable = False)
    bookstate = Column(Integer)

    def __init__(self,bookid=None, bookselector=None, bookstate = None):
        self.bookid = bookid
        self.bookselector = bookselector
        self.bookstate = bookstate


    def __repr__(self):
        return '<bookid:%r bookstate:%r>' % (self.bookid,self.bookstate)
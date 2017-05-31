from sqlalchemy import Column, Integer, String
from BookStore.database import Base

class Books(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(200),nullable = False)
    author = Column(String(200))
    editor = Column(String(200))
    count = Column(Integer)
    owner = Column(String(200))

    def __init__(self, name=None, author=None,editor=None,count=None,owner = None):
        self.name = name
        self.author = author
        self.editor = editor
        self.count = count
        self.owner = owner

    def __repr__(self):
        return '<Book: %r>' % (self.name)



class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
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
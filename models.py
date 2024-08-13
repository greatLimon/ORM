import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

# Tables
class Publisher(Base):
    __tablename__ = 'publisher'
    id = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length=60), unique=True)

class Shop(Base):
    __tablename__ = 'shop'
    id = sq.Column(sq.Integer, primary_key = True)
    name = sq.Column(sq.String(length=60), unique=True)

class Book(Base):
    __tablename__ = 'book'
    id = sq.Column(sq.Integer, primary_key = True)
    title = sq.Column(sq.String(length=60), unique=60)
    id_publisher = sq.Column(sq.ForeignKey('publisher.id'), nullable=False)
    publisher = relationship(Publisher, backref="Book")

class Stock(Base):
    __tablename__='stock'
    id = sq.Column(sq.Integer, primary_key = True)
    id_book = sq.Column(sq.ForeignKey('book.id'), nullable= False)
    id_shop = sq.Column(sq.ForeignKey('shop.id'), nullable= False)
    count = sq.Column(sq.Integer, nullable=False)
    book = relationship(Book, backref = 'book')
    shop = relationship(Shop, backref = 'shop')

class Sale(Base):
    __tablename__ = 'sale'
    id = sq.Column(sq.Integer, primary_key = True)
    price = sq.Column(sq.Float, nullable=False)
    date_sale = sq.Column(sq.Date, nullable=False)
    id_stock = sq.Column(sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer, nullable= False)
# -Tables

def recreate_tables(engine:sq.engine)->sq.orm.session.Session:
    Base.metadata.drop_all(engine)
    return create_tables(engine)

def create_tables(engine:sq.engine)->sq.orm.session.Session:
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind = engine)
    return Session()
    

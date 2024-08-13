import sqlalchemy
import json
import os
from models import recreate_tables ,create_tables, Publisher, Book, Shop, Sale, Stock

os.chdir(r'C:\Programs\MyPrograms\Netology\ORM\ORM')
def start_db()->sqlalchemy.orm.session.Session:
    basetype = 'postgresql'
    login = 'postgres'
    password = '123321'
    port = 'localhost:5432'
    base = 'netologyORM_db'
    DSN = f'{basetype}://{login}:{password}@{port}/{base}'
    # DSN = "postgresql://postgres:123321@localhost:5432/netologyORM_db"
    engine = sqlalchemy.create_engine(DSN)
    answ = input('Recreate tables?[y/n] ')
    if answ.lower() == 'y':
        return recreate_tables(engine)    
    return create_tables(engine)

def create_publiser(name:str, pk:int = -1)->Publisher:
    if pk <= 0: return Publisher(name = name)
    else: return Publisher(id = pk, name = name)
    
def create_book(title:str, id_publisher:int, pk:int = -1)->Book:
    if pk <= 0: return Book(title = title, id_publisher = id_publisher)
    else: return Book(id = pk, title = title, id_publisher = id_publisher)

def create_shop(name:str, pk:int = -1)->Shop:
    if pk <= 0: return Shop(name = name)
    else: return Shop(id = pk, name = name)

def create_stock(id_shop:int, id_book:int, count:int, pk:int = -1)->Stock:
    if pk <= 0: return Stock(id_shop = id_shop, id_book = id_book, count = count)
    else: return Stock(id = pk, id_shop = id_shop, id_book = id_book, count = count)

def create_sale(price:int, date_sale:str, count:int, id_stock:int, pk:int = -1)->Sale:
    if pk <= 0: return Sale(price = price, date_sale = date_sale, count = count, id_stock = id_stock)
    else: return Sale(id = pk, price = price, date_sale = date_sale, count = count, id_stock = id_stock)

def update_database(session:sqlalchemy.orm.session.Session, obj)->bool:
    session.add(obj)
    try:
        session.commit()
    except:
        return False
    return True
    # session.commit()

def upload_database(session:sqlalchemy.orm.session.Session)->bool:
    with open('tests_data.json', 'r') as json_file:
        data = json.load(json_file)
    for line in data:
        match line['model']:
            case 'publisher':
                obj = create_publiser(name=line['fields']['name'], pk=line['pk'])
                update_database(session=session, obj=obj)
            case 'book':
                obj = create_book(title=line['fields']['title'],id_publisher=line['fields']['id_publisher'], pk=line['pk'])
                update_database(session=session, obj=obj)
            case 'shop':
                obj = create_shop(name=line['fields']['name'], pk=line['pk'])
                update_database(session=session, obj=obj)
            case 'stock':
                obj = create_stock(id_shop=line['fields']['id_shop'], id_book=line['fields']['id_book'], count=line['fields']['count'], pk=line['pk'])
                update_database(session=session, obj=obj)
            case 'sale':
                obj = create_sale(price=line['fields']['price'], date_sale=line['fields']['date_sale'], count=line['fields']['count'], id_stock=line['fields']['id_stock'], pk=line['pk'])
                update_database(session=session, obj=obj)
    return True
    
def main():
    try:
        session = start_db()
    except:
        print('Error! I cant connect to DB')
        return False
    answ = input('Would you like to upload database from test data?[y/n] ')
    if answ.lower() == 'y':
        if upload_database(session):
            print('Success!')
        else: print('Error!')
    # start_db()


if __name__ == '__main__':
    main()
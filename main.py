import sqlalchemy
import psycopg2
from sqlalchemy.orm import sessionmaker
from models import create_tables

def start_db():
    basetype = 'postgresql'
    login = 'postgres'
    password = '123321'
    port = 'localhost:5432'
    base = 'netologyORM_db'
    DSN = f'{basetype}://{login}:{password}@{port}/{base}'
    # DSN = "postgresql://postgres:123321@localhost:5432/netologyORM_db"
    engine = sqlalchemy.create_engine(DSN)
    Session = sessionmaker(bind = engine)
    session = Session()    
    create_tables(engine)

def main():
    # try:
    #     start_db()
    # except:
    #     print('Error!')
    start_db()

if __name__ == '__main__':
    main()
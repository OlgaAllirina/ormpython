import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model import create_table, Stok, Sale, Shop, Book, Publisher

sql_sys = "postgresql"
login = "postgres"
password = "PWonlin3879"
host = "5432"
sql_base = "thirstwork_db"
DSN = f'{sql_sys}://{login}:{password}@localhost:{host}/{sql_base}'

engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()

create_table(engine) # создадим таблицу
session.close()

if __name__ == '__main__':
    pass





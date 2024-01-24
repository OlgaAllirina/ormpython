import sqlalchemy
import psycopg2
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from model import create_table, Stock, Sale, Shop, Book, Publisher

sql_sys = "postgresql"
login = "postgres"
password = "PWonlin3879"
host = "5432"
sql_base = "thirstwork_db"
DSN = f'{sql_sys}://{login}:{password}@localhost:{host}/{sql_base}'

engine = sqlalchemy.create_engine(DSN)

# создадим таблицу
create_table(engine)
# заполним таблицу данными

publisher1 = Publisher(name="Татьяна")
b1 = Book(title="Светочи тьмы", publisher=publisher1)
b2 = Book(title="Цербер-хранитель", publisher=publisher1)

publisher2 = Publisher(name="Карен")
b3 = Book(title="Прикосновения теней", publisher=publisher2)
b4 = Book(title="В оковах льда", publisher=publisher2)

shop1 = Shop(name="Читай-город")
stock1 = Stock(book=b1, shop=shop1, count="50")
sale1 = Sale(price="540", stock=stock1, date_sale="15.09.2023", count="5")
stock2 = Stock(book=b2, shop=shop1, count="35")
sale2 = Sale(price="670", stock=stock1, date_sale="12.01.2020", count="12")

shop2 = Shop(name="ДомКниг")
stock3 = Stock(book=b3, shop=shop2, count="27")
sale3 = Sale(price="472", stock=stock2, date_sale="31.05.2007", count="30")
stock4 = Stock(book=b2, shop=shop2, count="33")
sale4 = Sale(price="347", stock=stock2, date_sale="10.03.2008", count="9")

Session = sessionmaker(bind=engine)
session = Session()
# зарегистрируем изменения
session.add_all([publisher1, shop1, shop2, stock1, stock2, sale1, sale2, b1, b2, publisher2, stock3, stock4, sale3,
                 sale4, b3, b4])
session.commit()
# обязательный параметр ввода
name_or_id = input("Введите имя или id автора: ")
# объединяем таблицы и выводим необходимую информацию
if name_or_id.isdigit():
    q = session.query(Book, Shop, Sale).select_from(Book).join(Stock).join(Publisher).join(Shop).join(Sale).filter(
        Publisher.id == name_or_id)
    for bo, sh, sa in q.all():
        print(bo, sh, sa)
else:
    q = session.query(Book, Shop, Sale).select_from(Stock).join(Book).join(Publisher).join(Shop).join(Sale).filter(
        Publisher.name == name_or_id)
    print(q)
    for bo, sh, sa in q.all():
        print(bo, sh, sa)
session.close()


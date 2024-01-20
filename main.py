import sqlalchemy
import psycopg2
from sqlalchemy.orm import sessionmaker
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

publisher1 = Publisher(name="Татьяна", books=[
    Book(title="Не буди ведьму"),
    Book(title="Ведьмин круг"),
    Book(title="Беги, ведьма")])
publisher2 = Publisher(name="Карен", books=[
    Book(title="Тайны рукописи"),
    Book(title="В оковах льда"),
    Book(title="Рождённая огнём")])
b1 = Book(title="Светочи тьмы", publisher=publisher1)
b2 = Book(title="Цербер-хранитель", publisher=publisher1)
b3 = Book(title="Прикосновения теней", publisher=publisher2)

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
session.add_all([publisher1, publisher2, shop1, shop2, stock1, stock2, stock3, stock4, sale1, sale2, sale3, sale4])
session.commit()

name_or_id = input("Введите имя или id автора: ")
if name_or_id.isdigit():
    query = session.query(Book).join(Stock).join(Shop).join(Sale).join(Publisher).filter(Publisher.id == name_or_id).all()


# "название книги | название магазина, в котором была куплена эта книга | стоимость покупки | дата покупки"


session.close()


import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), unique=True)

    books = relationship("Book", backref="publishers")

    def __str__(self):
        return f'{self.id} : {self.name}'


class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=50), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publishers = relationship(Publisher, backref="books")
    stoks = relationship("Stok", backref="books")

    def __str__(self):
        return f'{self.id} : ({self.title}, {self.id_publisher})'


class Stok(Base):
    __tablename__ = "stok"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    books = relationship("Book", backref="stoks")
    shops = relationship("Shop", backref="stoks")
    sales = relationship("Sale", backref="stoks")

    def __str__(self):
        return f'{self.id} : ({self.id_book}, {self.id_shop}, {self.count})'


class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=60), unique=True)

    stoks = relationship("Stok", backref="shops")

    def __str__(self):
        return f'{self.id} : {self.name}'


class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=False)
    date_sales = sq.Column(sq.Integer, nullable=False)
    id_stok = sq.Column(sq.Integer, sq.ForeignKey("stok"), nullable=False)
    count = sq.Column(sq.Integer, nullable=False)

    stoks = relationship("Stok", backref="sales")

    def __str__(self):
        return f'{self.id} : ({self.price}, {self.date_sales}, {self.count}, {self.stok})'


def create_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

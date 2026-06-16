from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float


class Base(DeclarativeBase):
    pass


class Order(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)

    order_id = Column(String)

    customer = Column(String)

    status = Column(String)


class Invoice(Base):

    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True)

    order_id = Column(String)

    amount = Column(Float)


class Inventory(Base):

    __tablename__ = "inventory"

    id = Column(Integer, primary_key=True)

    product = Column(String, unique=True)

    stock = Column(Integer)
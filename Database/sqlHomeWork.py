import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import create_engine, Session

from Database.sqlalchemy_test import Base

engine = create_engine('/web/Sqlite-Data/example.db')

session = Session(bind=engine)


# Customer table
class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    address = Column(String(200), nullable=False)
    town = Column(String(50), nullable=False)
    created_on = Column(DateTime(), default=datetime.time)
    updated_on = Column(DateTime(), default=datetime.time, onupdate=datetime.time)


c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c2 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )

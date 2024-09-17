from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

Base_order = declarative_base()

class Order(Base_order):
    __tablename__ = 'Orders'

    id = Column(Integer, primary_key=True)
    customer_name = Column(String, nullable=False)
    orders = Column(String, nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow)

    def toJSON(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'orders': self.orders,
            'date_created': self.date_created.strftime('%Y-%m-%d %H:%M:%S')
        }

from sqlalchemy import Column, Integer, String

from app.db.database import Base


class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True, index=True)
    customer_name = Column(String)
    customer_email = Column(String)

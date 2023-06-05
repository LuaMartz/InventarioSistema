from sqlalchemy import Column, Integer, String, Float
from config.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    brand = Column(String)
    description = Column(String)
    price = Column(Float)
    entry_date = Column(String)
    availability = Column(String)
    available_quantity = Column(Integer)
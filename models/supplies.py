from sqlalchemy import Column, ForeignKey, Integer, Float
from config.database import Base

class Supplies(Base):
    __tablename__ = "supplies"

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    purchase_price = Column(Float)
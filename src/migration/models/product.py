from sqlalchemy import Integer, String, Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

product_category_association_table = Table(
    'product_category', Base.metadata,
    Column('product_id', Integer, ForeignKey('product.id')),
    Column('category_id', Integer, ForeignKey('category.id'))
)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    language = Column(String(50))
    barcode = Column(String(100))
    category = relationship('Category', secondary=product_category_association_table)


from sqlalchemy import Integer, String, Column, create_engine, ForeignKey, Table
from sqlalchemy.orm import relationship, joinedload, subqueryload, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = None
session = None


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    tag = Column(String(50), unique=True)
    name = Column(String(50))


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

    def __init__(self, json):
        self.name = json['product_name'] if 'product_name' in json else None
        self.language = json['lang'] if 'lang' in json else None
        self.barcode = json['code'] if 'code' in json else None
        if 'categories_tags' in json and 'categories' in json:
            for (tag, name) in zip(json['categories_tags'], json['categories'].split(',')):
                self.category.append(Category(tag=tag, name=name))


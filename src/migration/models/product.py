from sqlalchemy import Integer, String, Column, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

product_category_association_table = Table(
    'product_category', Base.metadata,
    Column('product_id', Integer, ForeignKey('product.id')),
    Column('category_id', Integer, ForeignKey('category.id'))
)
product_origins_association_table = Table(
    'product_country_origin', Base.metadata,
    Column('product_id', Integer, ForeignKey('product.id')),
    Column('country_id', Integer, ForeignKey('country.id'))
)
product_selling_association_table = Table(
    'product_country_selling', Base.metadata,
    Column('product_id', Integer, ForeignKey('product.id')),
    Column('country_id', Integer, ForeignKey('country.id'))
)
product_brand_association_table = Table(
    'product_brand', Base.metadata,
    Column('product_id', Integer, ForeignKey('product.id')),
    Column('brand_id', Integer, ForeignKey('brand.id'))
)
product_additive_association_table = Table(
    'product_additive', Base.metadata,
    Column('product_id', Integer, ForeignKey('product.id')),
    Column('additive_id', Integer, ForeignKey('additive.id'))
)


class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    language = Column(String(50))
    barcode = Column(String(100))
    category = relationship('Category', secondary=product_category_association_table)
    origin_country = relationship('Country', secondary=product_origins_association_table)
    selling_country = relationship('Country', secondary=product_selling_association_table)
    brand = relationship('Brand', secondary=product_brand_association_table)
    additive = relationship('Additive', secondary=product_additive_association_table)


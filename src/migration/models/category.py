from sqlalchemy import Integer, String, Column
from .product import Base


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    tag = Column(String(50), unique=True)
    name = Column(String(50), unique=True)




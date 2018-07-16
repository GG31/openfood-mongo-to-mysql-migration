from sqlalchemy import Integer, String, Column
from .product import Base


class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True)
    tag = Column(String(50), unique=True)
    name = Column(String(50), unique=True)




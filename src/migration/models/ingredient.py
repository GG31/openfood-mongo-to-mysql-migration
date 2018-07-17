from sqlalchemy import Integer, String, Column
from .product import Base


class Ingredient(Base):
    __tablename__ = 'ingredient'
    id = Column(Integer, primary_key=True)
    tag = Column(String(50), unique=True)
    name = Column(String(50), unique=True)


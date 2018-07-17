from sqlalchemy import Integer, String, Column, Boolean
from ..product_model import Base


class Ingredient(Base):
    __tablename__ = 'ingredient'
    id = Column(Integer, primary_key=True)
    tag = Column(String(50), unique=True)
    name = Column(String(50), unique=True)
    is_allergen = Column(Boolean(50), default=False)


from sqlalchemy import Integer, String, Column
from ..product_model import Base


class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key=True)
    tag = Column(String(50), unique=True)
    name = Column(String(50), unique=True)

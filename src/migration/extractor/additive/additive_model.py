from sqlalchemy import Integer, String, Column
from ..product_model import Base


class Additive(Base):
    __tablename__ = 'additive'
    id = Column(Integer, primary_key=True)
    tag = Column(String(50), unique=True)


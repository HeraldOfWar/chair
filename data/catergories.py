from sqlalchemy import orm
from sqlalchemy import Column, Integer, String
from data.db_session import SqlAlchemyBase


class Category(SqlAlchemyBase):
    """Модель категории"""
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), unique=True)
    products = orm.relationship('Product', back_populates='category')  # привязываем товары к категории

    def __repr__(self):
        return f'<Category> {self.name}'

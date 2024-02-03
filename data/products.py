from sqlalchemy import orm, ForeignKey, Column
from sqlalchemy import Integer, String, Numeric, ARRAY
from data.db_session import SqlAlchemyBase


class Product(SqlAlchemyBase):
    """Модель товара"""
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    price = Column(Numeric)  # актуальная цена, выгруженная с магазина
    link = Column(String(255))  # ссылка на товар в магазине
    category_id = Column(Integer, ForeignKey("categories.id"))  # внешний ключ id категории
    category = orm.relationship('Category', back_populates='products')  # привязываем товар к категории
    params = Column(String(255))  # путь к json-файлу с характеристиками товара
    images = Column(ARRAY(String(255)))  # список путей к изображениям товара
    model_3d = Column(String(255))  # путь к 3д-модели товара
    link = Column(String)  # общее описание товара

    def __repr__(self):
        return f'<Product> {self.name}'

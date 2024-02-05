from sqlalchemy import orm, ForeignKey, Column
from sqlalchemy import Integer, String, Numeric
from sqlalchemy_serializer import SerializerMixin
from data.db_session import SqlAlchemyBase


class Product(SqlAlchemyBase, SerializerMixin):
    """Модель товара"""
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(127))
    company = Column(String(45))  # название производителя
    link = Column(String(127))  # ссылка на товар в магазине
    price = Column(Numeric)  # актуальная цена, выгруженная с магазина
    category_id = Column(Integer, ForeignKey("categories.id"))  # внешний ключ id категории
    category = orm.relationship('Category', back_populates='products')  # привязываем товар к категории
    params = Column(String(45))  # путь к json-файлу с характеристиками товара
    images = Column(String(255))  # список путей к изображениям товара
    model_3d = Column(String(45))  # путь к 3д-модели товара
    description = Column(String(2046))  # общее описание товара

    def __repr__(self):
        return f'<Product> {self.name}'

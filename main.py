from os import environ
from flask import Flask, send_file
from flask_restful import Api
from werkzeug.security import safe_join

from api import product_resources
from data import db_session


app = Flask(__name__)  # создаем приложение
app.config['SECRET_KEY'] = 'chair-hackaton'

api = Api(app)  # создаем апи-ресурс
api.add_resource(product_resources.ProductResource, '/api/products/<int:product_id>')  # товар
api.add_resource(product_resources.ProductsListResource, '/api/products')  # каталог товаров

db_session.global_init('db/chair.db')  # инициализируем базу данных

port = int(environ.get("PORT", 8080))
app.run(host='0.0.0.0', port=port)  # запускаем сервер

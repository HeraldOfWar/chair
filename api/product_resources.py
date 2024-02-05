from os import environ
from boto3 import client
from botocore.config import Config
from flask_restful import Resource, abort
from flask import jsonify, send_file
from data import db_session
from data.products import Product


def abort_if_product_not_found(product_id: int):
    """Обработка в ситуации, когда записи с указанным id не существует"""
    session = db_session.create_session()
    product = session.query(Product).get(product_id)
    if not product:
        abort(404, message=f"Product {product_id} not found")  # ошибка 404, json {not found}


# def get_file(filename: str, bucket_name: str):
#     s3 = client('s3',
#                endpoint_url=environ['MINIO_HOST'],
#                aws_access_key_id=environ['MINIO_ROOT_USER'],
#                aws_secret_access_key=environ['MINIO_ROOT_PASSWORD'],
#                config=Config(
#                    signature_version='s3v4'))  # создали объект для управления файловым хранилищем
#     s3.download_file(bucket_name, filename, f'img/{filename}')


class ProductResource(Resource):
    """Ресурс товара (restful-api)"""

    def get(self, product_id: int):
        """Получение Товара"""
        abort_if_product_not_found(product_id)
        session = db_session.create_session()
        product = session.query(Product).get(product_id)
        return jsonify({'product': product.to_dict(
            only=('name', 'price', 'link', 'company', 'category.name',
                  'params', 'images', 'model_3d', 'description'))})

    # def post(self, product_id: int):
    #     """Выгрузка файлов"""
    #     for f in listdir('img'):
    # 	    remove(join('img', f))
    #     abort_if_product_not_found(product_id)
    #     args = product_parser.parse_args()  # парсер аргументов
    #     if args.get('images'):
    #         for img in args['images']:
    #             get_file(args['images'][0], 'images')
    #         return send_file(f'img/{args["images"][0]}')

    # def delete(self, product_id: int):
    #     """Удаление товара"""
    #     abort_if_product_not_found(product_id)
    #     session = db_session.create_session()
    #     product = session.query(Product).get(product_id)
    #     session.delete(product)
    #     session.commit()
    #     return jsonify({'success': 'OK'})


class ProductsListResource(Resource):
    """Ресурс списка товаров (restful-api)"""

    def get(self):
        """Получение всех товаров"""
        session = db_session.create_session()
        product = session.query(Product).all()
        return jsonify({'products': [item.to_dict(
            only=('name', 'price', 'company', 'images'))
            for item in product]})  # возвращаем json со всеми записями

    # def post(self):
    #     """Публикация нового товара"""
    #     args = product_parser.parse_args()
    #     session = db_session.create_session()
    #     product = Product(
    #         name=args['name'],
    #         company=args['company'],
    #         price=args['price'],
    #         link=args['link'],
    #         category_id=args['category_id'],
    #         params=args['link'],
    #         images=args['link'],
    #         model_3d=args['link'],
    #         description=args['description']
    #     )
    #     session.add(product)
    #     session.commit()
    #     return jsonify({'success': 'OK'})

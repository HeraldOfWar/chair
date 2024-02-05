from flask_restful import reqparse
from werkzeug.datastructures import FileStorage

product_parser = reqparse.RequestParser()
product_parser.add_argument('params')
product_parser.add_argument('images', action='append')
product_parser.add_argument('model_3d')


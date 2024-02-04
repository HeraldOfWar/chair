import os
import boto3
from botocore.client import Config
from flask import Flask
from data import db_session

app = Flask(__name__)  # создаём приложение Flask
db_session.global_init('db/chair.db')  # инициализируем базу данных
port = int(os.environ.get("PORT", 8080))  # порт
app.run(host='0.0.0.0', port=port)  # запуск


remote_url = os.getenv('REMOTE_URL')
minio_host = os.getenv('MINIO_HOST')
minio_port = os.getenv('MINIO_PORT')
minio_url = f'{minio_host}:{minio_port}'

minio_user = os.getenv('MINIO_USER')
minio_password = os.getenv('MINIO_PASSWORD')

s3 = boto3.client('s3',
                  endpoint_url=os.environ['MINIO_HOST'],
                  aws_access_key_id=os.environ['MINIO_ROOT_USER'],
                  aws_secret_access_key=os.environ['MINIO_ROOT_PASSWORD'],
                  config=Config(signature_version='s3v4'))  # создали объект для управления файловым хранилищем

bucket_name = 'product-images'


@app.route('/')
def index():
    return 'Hello World'
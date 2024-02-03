import os
import boto3
from botocore.client import Config
from flask import Flask
from data import db_session


if __name__ == '__main__':
    s3 = boto3.resource('s3',
                        endpoint_url=os.environ['MINIO_HOST'],
                        aws_access_key_id=os.environ['MINIO_ROOT_USER'],
                        aws_secret_access_key=os.environ['MINIO_ROOT_PASSWORD'],
                        config=Config(signature_version='s3v4'))  # создали объект для управления файловым хранилищем
    app = Flask(__name__)  # создаём приложение Flask
    db_session.global_init('db/chair.db')  # инициализируем базу данных
    port = int(os.environ.get("PORT", 5000))  # порт
    app.run(host='0.0.0.0', port=port)  # запуск

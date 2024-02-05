FROM python:3.11-slim

WORKDIR /server

COPY . ./

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/server/main.py"]
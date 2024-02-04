FROM python:3.11-slim

WORKDIR /server

COPY main.py ./data/ ./db/ requirements.txt ./

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/server/main.py"]
FROM python:3.8-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY crawler.py mongo.py ./

CMD [ "python3", "crawler.py"]
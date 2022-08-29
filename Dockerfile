FROM python:3.7.11-slim

COPY ./.docker/python/requirements.txt .

RUN pip install -r requirements.txt

COPY ./code /code

WORKDIR /code

ENTRYPOINT [ "python","app.py" ]
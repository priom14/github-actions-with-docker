FROM python:3.9-slim

COPY . /app

WORKDIR /app

RUN pip install flask

EXPOSE 5000

CMD [ "python", "app.py" ]
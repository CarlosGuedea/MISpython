FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y msodbcsql

ENV PYTHONUNBUFFERED 1

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
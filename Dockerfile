FROM python:3.8 AS base

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

COPY start.sh /app/start.sh

RUN chmod +x /app/start.sh


CMD ["/app/start.sh"]

FROM python:3.12

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir scrapy psycopg2 selenium django

EXPOSE 8080

# CMD ["python", "server.py"]
# CMD ["scrapy", "crawl", "spiders/sreality_spider.py"]
CMD ["python", "server.py"]

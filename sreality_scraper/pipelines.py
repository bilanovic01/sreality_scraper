# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
class PostgreSQLPipeline:
    def open_spider(self, spider):
        self.connection = psycopg2.connect(
            dbname='mydatabase',
            user='postgres',
            password='password',
            host='127.0.0.1',
            port='5432'
        )
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        sql = "INSERT INTO flats (title, image_url) VALUES (%s, %s)"
        self.cursor.execute(sql, (item['title'], item['image_url']))
        return item

class SrealityScraperPipeline:
    def process_item(self, item, spider):
        return item

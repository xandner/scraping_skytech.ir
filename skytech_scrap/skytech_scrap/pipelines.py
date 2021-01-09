# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3


class SkytechScrapPipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn=sqlite3.connect('database.db')
        self.curr=self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" CREATE TABLE IF NOT EXISTS my_table(
            pro_name TEXT,
            pro_price TEXT,
            pro_number TEXT
         )""")

    def insert_data(self, item):
        self.curr.execute(""" INSERT INTO my_table VALUES (?,?,?)""",(
            item['name'][0],
            item['price'][0],
            item['number'][0],
        ))

    def process_item(self, item, spider):
        self.insert_data(item)
        return item

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
        self.conn = sqlite3.connect('database.db')
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute(""" CREATE TABLE IF NOT EXISTS my_table(
            pro_name TEXT,
            pro_price TEXT,
            pro_number TEXT,
            picture TEXT
         )""")

    def insert_data(self, item):

        if len(item['name']) >= 1:
            name = []
            price = []
            number = []
            image = []
            for i in item['name']:
                name.append(i)
            for i in range(0, len(item['price']), 3):
                price.append(item['price'][i])
            for i in range(2, len(item['number']), 3):
                number.append(item['number'][i])
            for i in item['image']:
                image.append(i)
            for i in range(len(name)):
                self.curr.execute("""insert into my_table values (?,?,?,?)""", (
                    name[i],
                    price[i],
                    number[i],
                    image[i]
                ))
                self.conn.commit()
        else:
            self.curr.execute("""insert into my_table values (?,?,?,?)""", (
                item['name'][0],
                item['price'][0],
                item['price'][2],
                item['image'][0]
            ))
            self.conn.commit()

    def sort_data(self, name, item):
        for i in name:
            self.insert_name(i)
        for i in item:
            self.insert_price(i)

    def process_item(self, item, spider):
        self.insert_data(item)
        return item

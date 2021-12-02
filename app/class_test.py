from myclass.Crawler import Crawler
from myclass.Mongo import MongoConnect

fiis = Crawler()

fiis_list = fiis.get_fii_list()


fiis.add_price_data_to_table(fiis_list)

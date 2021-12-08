from myclass.Crawler import Crawler,MongoClass


fiis = Crawler()

fiis_list = fiis.get_fii_list()


conn = MongoClass()

conn.add_price_data_to_table(fiis_list)



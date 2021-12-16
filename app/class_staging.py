from myclass.Crawler import Crawler


fiis = Crawler()

var2 = fiis.get_fii_list()

fiis_list = fiis.get_fii_list()


fiis.add_price_data_to_table(fiis_list,"collect")




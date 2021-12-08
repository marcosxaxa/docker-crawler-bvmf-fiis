import unittest

from Crawler import Crawler


class TestFiis(unittest.TestCase,Crawler):

    def test_list_fiis(self):
        fiis_list = Crawler.get_fii_list(self)
        self.assertIn("BCFF11", fiis_list)

    def test_get_price(self):
        ticker = "bcff11"
        fii_price = Crawler.get_price(self,ticker)
        print(fii_price)
        assert type(fii_price) is dict 

if __name__ == '__main__':
    unittest.main()
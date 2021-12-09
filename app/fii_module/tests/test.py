import os
from unittest import TestCase, mock
import unittest

from myclass.Crawler import Crawler


class TestFiis(TestCase,Crawler):
    @mock.patch.dict(os.environ, {"DB_NAME": "dev", "DB_PASSWORD": "dev-user", "DB_USERNAME": "dev-user" })

    def test_list_fiis(self):
        username = ""
        password = ""
        db_name = ""

        fiis_list = Crawler.get_fii_list(self)
        self.assertIn("BCFF11", fiis_list)

    def test_get_price(self):
        ticker = "bcff11"
        fii_price = Crawler.get_price(self,ticker)
        # print(fii_price)
        assert type(fii_price) is dict 
        assert fii_price["ticker"] == ticker
        assert type(fii_price["eod_price"]) is float

if __name__ == '__main__':
    unittest.main()
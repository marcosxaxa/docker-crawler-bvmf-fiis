import os

password = os.environ["DB_PASSWORD"] = "test"
db_name = os.environ["DB_NAME"] = "test"
username = os.environ["DB_USERNAME"] = "test"

from myclass.Crawler import Crawler


def test_list_fiis():
    crawler_class = Crawler()
    fiis_list = crawler_class.get_fii_list()
    assert "BCFF11" in fiis_list



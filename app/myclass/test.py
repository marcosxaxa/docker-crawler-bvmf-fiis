import unittest

import Crawler

class TestGetFii(unittest.TestCase):
    def test_get_fii(self):
        """
        Test the get fii func
        """

        fii_list = Crawler.Crawler.get_fii_list(self)
        self.assertIn("BCFF11", fii_list)

if __name__ == '__main__':
    unittest.main()
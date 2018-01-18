from .context import malshare
import unittest


class ConnectTestSuite(unittest.TestCase):

    def test_malshare_feed_item(self):
        data = malshare.Malshare.get_latest()
        self.assertEqual(data[0].__class__.__name__, 'Malshare', 'Datatype mis-matched.')

    def test_malshare_feed_count(self):
        data = malshare.Malshare.get_all_dates()
        self.assertGreater(len(data), 50, 'Number of items found in feed.')


if __name__ == '__main__':
    unittest.main()

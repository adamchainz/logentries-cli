#!/usr/bin/env python
from datetime import datetime, timedelta
import imp
import unittest


class LogentriesTest(unittest.TestCase):
    """
    Tests are rather minimal - it's much better to test the tool
    against the logentries API but there is no public sandbox.
    """

    @classmethod
    def setUpClass(cls):
        super(LogentriesTest, cls).setUpClass()
        cls.mod = imp.load_source('logentries', 'bin/logentries')

    def test_its_a_module(self):
        self.assertTrue(self.mod.__name__)

    def test_as_logentries_timestamp(self):
        as_let = self.mod.as_logentries_timestamp
        self.assertEqual(as_let(datetime(1970, 1, 1)), 0)
        self.assertEqual(as_let(datetime(2015, 1, 1)), 1420070400000)

    def test_parse_datetime(self):
        parse_dt = self.mod.parse_datetime
        self.assertEqual(
            parse_dt('2015-01-01'),
            datetime(2015, 1, 1)
        )
        self.assertEqual(
            parse_dt('3 hours ago'),
            (datetime.now() - timedelta(hours=3)).replace(microsecond=0)
        )


if __name__ == '__main__':
    unittest.main()

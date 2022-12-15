import unittest

from AppExceptions import IncorrectInputError
from api import *
from util import check_input


class MyTestCase(unittest.TestCase):

    def test_regexp_fail(self):
        self.assertRaises(IncorrectInputError, check_input, "fsfsdf")
        self.assertRaises(IncorrectInputError, check_input, "115.2.3")
        self.assertRaises(IncorrectInputError, check_input, "120.")
        self.assertRaises(IncorrectInputError, check_input, "117 000 000")
        self.assertRaises(IncorrectInputError, check_input, "117 000 000")

    def test_regexp_ok(self):
        try:
            check_input("117")
            check_input("117.01")
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_api_get_cur_fail(self):
        self.assertRaises(Exception, get_cur, ["btc", ""])
        self.assertRaises(Exception, get_cur, ["tc", "aaa"])

    def test_api_get_cur_ok(self):
        try:
            get_cur("BTC", "BTS")
            get_cur("BTS", "BTC")
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_get_btc_to_bts_fail(self):
        self.assertRaises(IncorrectInputError, get_btc_to_bts, "fsfsdf")
        self.assertRaises(IncorrectInputError, get_btc_to_bts, "115.2.3")
        self.assertRaises(IncorrectInputError, get_btc_to_bts, "120.")
        self.assertRaises(IncorrectInputError, get_btc_to_bts, "117 000 000")

    def test_get_btc_to_bts_ok(self):
        try:
            get_btc_to_bts("117")
            get_btc_to_bts("117.01")
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_get_bts_to_btc_fail(self):
        self.assertRaises(IncorrectInputError, get_bts_to_btc, "fsfsdf")
        self.assertRaises(IncorrectInputError, get_bts_to_btc, "115.2.3")
        self.assertRaises(IncorrectInputError, get_bts_to_btc, "120.")
        self.assertRaises(IncorrectInputError, get_bts_to_btc, "117 000 000")

    def test_get_bts_to_btc_ok(self):
        try:
            get_bts_to_btc("117")
            get_bts_to_btc("117.01")
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()

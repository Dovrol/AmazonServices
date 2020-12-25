import unittest


class MyTest(unittest.TestCase):
    def test_upper(self):
        assert "foo".upper() == "FOO", "Not upper"



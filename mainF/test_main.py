import unittest
from main import add, subtract


class MyTestCase(unittest.TestCase):
    def test_add(self):
        result = add(5,5)
        expect = 10
        self.assertEqual(expect, result)  # add assertion here

    def test_subtract(self):
        result = subtract(10,5)
        expect = 5
        self.assertEqual(expect,result)


if __name__ == '__main__':
    unittest.main()

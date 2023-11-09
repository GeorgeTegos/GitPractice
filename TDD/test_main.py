import unittest
from main import add, subtract, multiply, divide


class MyTestCase(unittest.TestCase):

    def test_add(self):
        expect = 10
        result = add(3, 7)
        self.assertEqual(expect, result)  # add assertion here

    def test_add_wrong_type(self):
        self.assertEqual(None, add(3,"4"))

    def test_subtract(self):
        expect = 5
        result = subtract(7, 2)
        self.assertEqual(expect, result)

    def test_subtract_wrong_type(self):
        self.assertEqual(None, subtract("2", 1))

    def test_multiply(self):
        expect = 24
        result = multiply(2, 12)
        self.assertEqual(expect, result)

    def test_multiply_wrong_type(self):
        self.assertEqual(TypeError, multiply("2", 2))

    def test_divide(self):
        expect = 5.0
        result = divide(25, 5)
        self.assertEqual(expect, result)

    def test_divide_wrong_type(self):
        self.assertEqual(None, divide(25, "2"))

    def test_divide_returns_float(self):
        expect = True
        result = divide(25, 2)
        result = isinstance(result, float)
        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()

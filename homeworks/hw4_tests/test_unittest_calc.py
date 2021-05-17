import unittest
from calculator import add, subtract, multiply, divide


class TestCalc(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-10, 3), -7)
        self.assertRaises(TypeError, add, '8', 5)
        self.assertRaises(TypeError, add, 8, '5')

    def test_sub(self):
        self.assertEqual(subtract(4, 2), 2)
        self.assertEqual(subtract(-2, 2), -4)
        self.assertEqual(subtract(-2, -2), 0)
        self.assertRaises(TypeError, subtract, '8', 5)
        self.assertRaises(TypeError, subtract, 8, '5')

    def test_mul(self):
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(2, 0), 0)
        self.assertEqual(multiply(-2, -2), 4)
        self.assertEqual(multiply(-2, 2), -4)
        self.assertEqual(multiply('8', 5), '88888')
        self.assertEqual(multiply(8, '5'), '55555555')
        self.assertRaises(TypeError, multiply, '8', '5')

    def test_div(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(10, -5), -2)
        self.assertEqual(divide(-10, -5), 2)
        self.assertRaises(ValueError, divide, 2, 0)
        self.assertRaises(TypeError, divide, '8', 5)
        self.assertRaises(TypeError, divide, 8, '5')


if __name__ == '__main__':
    unittest.main()

import unittest
import unittesting


class TestCalc(unittest.TestCase):

    def test_add(self):  # all test should start with test instead of something else
        result = unittesting.add(10, 5)
        self.assertEqual(result, 15)
        result = unittesting.add(10, 5)

        self.assertEqual(unittesting.add(-1, -1), -2)
        self.assertEqual(unittesting.add(-1, 1), 0)

    def test_subtract(self):  # all test should start with test instead of something else
        self.assertEqual(unittesting.subtract(10, 5), 5)
        self.assertEqual(unittesting.subtract(-1, 1), -2)
        self.assertEqual(unittesting.subtract(-1, -1), 0)

    def test_multiply(self):  # all test should start with test instead of something else
        self.assertEqual(unittesting.multiple(10, 5), 50)
        self.assertEqual(unittesting.multiple(-1, 1), -1)
        self.assertEqual(unittesting.multiple(-1, -1), 1)

    def test_divide(self):  # all test should start with test instead of something else
        self.assertEqual(unittesting.divide(10, 5), 2)
        self.assertEqual(unittesting.divide(-1, 1), -1)
        self.assertEqual(unittesting.divide(-1, -1), 1)

        self.assertRaises(ValueError, unittesting.divide,10,0)  # leave off the parenthesis because we pass in each arg

        with self.assertRaises(ValueError):
            unittesting.divide(10,0)


if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()

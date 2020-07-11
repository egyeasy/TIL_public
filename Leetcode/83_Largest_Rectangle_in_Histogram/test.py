import unittest
import solution


class Test(unittest.TestCase):
    def setUp(self):
        self.instance = solution.Solution()

    def test1(self):
        result = self.instance.largestRectangleArea([])
        self.assertEqual(result, 0)

    def test2(self):
        result = self.instance.largestRectangleArea([2, 1, 5, 6, 2, 3])
        self.assertEqual(result, 10)

    def test3(self):
        result = self.instance.largestRectangleArea([2, 2, 2, 2])
        self.assertEqual(result, 8)

    def test4(self):
        result = self.instance.largestRectangleArea([1] * 500000000)
        self.assertEqual(result, 500000000)


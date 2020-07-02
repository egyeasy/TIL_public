import unittest
import solution2


class Test(unittest.TestCase):
    def setUp(self):
        self.solution = solution2.Solution()

    def test1(self):
        result = self.solution.lengthOfLastWord("Hello World")
        self.assertEqual(result, 5)

    def test2(self):
        result = self.solution.lengthOfLastWord("hi ")
        self.assertEqual(result, 2)

    def test3(self):
        result = self.solution.lengthOfLastWord(" i ")
        self.assertEqual(result, 1)

    def test4(self):
        result = self.solution.lengthOfLastWord(" ")
        self.assertEqual(result, 0)

    def test5(self):
        result = self.solution.lengthOfLastWord("")
        self.assertEqual(result, 0)

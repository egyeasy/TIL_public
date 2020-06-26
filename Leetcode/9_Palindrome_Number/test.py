import unittest
import solution


class Test(unittest.TestCase):
    def test(self):
        instance = solution.Solution()
        result = instance.isPalindrome(1234)
        self.assertEqual(result, False)
    def test2(self):
        instance = solution.Solution()
        result = instance.isPalindrome(121)
        self.assertEqual(result, True)
    def test3(self):
        instance = solution.Solution()
        result = instance.isPalindrome(-121)
        self.assertEqual(result, False)
    def test4(self):
        instance = solution.Solution()
        result = instance.isPalindrome(0)
        self.assertEqual(result, True)
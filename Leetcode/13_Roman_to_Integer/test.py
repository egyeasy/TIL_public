import unittest
import solution


class Test(unittest.TestCase):
    def setUp(self):
        self.instance = solution.Solution()

    def test(self):
        result = self.instance.romanToInt("LVIII")
        self.assertEqual(result, 58)

    def test2(self):
        result = self.instance.romanToInt("III")
        self.assertEqual(result, 3)

    def test3(self):
        result = self.instance.romanToInt("IV")
        self.assertEqual(result, 4)

    def test4(self):
        result = self.instance.romanToInt("MCMXCIV")
        self.assertEqual(result, 1994)


testSuite = unittest.TestSuite()
for testmethod in ("test", "test2", "test3", "test4"):
    testSuite.addTest(Test(testmethod))
runner = unittest.TextTestRunner()
runner.run(testSuite)

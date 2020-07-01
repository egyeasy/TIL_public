import unittest
import solution

class Test(unittest.TestCase):
    def setUp(self):
        self.instance = solution.Solution()

    def test(self):
        result = self.instance.isValid("()")
        self.assertEqual(result, True)

    def test2(self):
        result = self.instance.isValid("()[]{}")
        self.assertEqual(result, True)

    def test3(self):
        result = self.instance.isValid("(]")
        self.assertEqual(result, False)

    def test4(self):
        result = self.instance.isValid("([)]")
        self.assertEqual(result, False)

    def test5(self):
        result = self.instance.isValid("{[]}")
        self.assertEqual(result, True)
    def test6(self):
        result = self.instance.isValid("")
        self.assertEqual(result, True)


testSuite = unittest.TestSuite()
for testmethod in ("test", "test2", "test3", "test4", "test5", "test6"):
    testSuite.addTest(Test(testmethod))
runner = unittest.TextTestRunner()
runner.run(testSuite)
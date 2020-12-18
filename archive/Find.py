import unittest
from Find_Module1 import TestRecommend
from Find_Module2 import TestDeficiency
def my_suite():
    suite=unittest.TestSuite()
    result=unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestRecommend))
    suite.addTest(unittest.makeSuite(TestDeficiency))
    runner=unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()
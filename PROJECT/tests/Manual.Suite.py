import unittest
from testperson_final import TestMP
from testcereal_final import TestMC1

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestMP))
    suite.addTest(unittest.makeSuite(TestMC1))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
my_suite()
import calgrade
import unittest

class Test_calgrade(unittest.TestCase):
    def testcalGradeA(self):
        self.assertEqual(calgrade.calGrade(80),"A") 

    def testcalGradeF(self):
        self.assertEqual(calgrade.calGrade(49),"F")  

    def testcalGradeC(self):
        self.assertEqual(calgrade.calGrade(59),"D") 

    # def testMultiplyFunction(self):
    #     self.assertEqual(multiply(1,2),2) 

    # def testDivideFunction(self):
    #     self.assertEqual(divide(100,10), 10)
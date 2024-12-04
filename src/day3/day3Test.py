import unittest
from .day3 import doMul, sumValidMuls, sumValidMulWithSwitches
class Day3UnitTest(unittest.TestCase):
    # Basic doMul
    def testDoMul(self):
        self.assertEqual(doMul("mul(1,1)"), 1)
        self.assertEqual(doMul("mul(2,2)"), 4)
        self.assertEqual(doMul("mul(10,5)"), 50)

    # sumValidMuls

    def testSumValidMulSingle(self):
        self.assertEqual(sumValidMuls("mul(2,2)"), 4)

    def testSumvalidMulsSingleWithJunk(self):
        self.assertEqual(sumValidMuls("adfamul(2,2)adf"), 4)

    def testSumValidMulsMultiple(self):
        self.assertEqual(sumValidMuls("mul(2,2)mul(3,3)"), 13)

    def testSumValidMulsMultipleWithJunk(self):
        self.assertEqual(sumValidMuls("33amul(2,2)asdmul(3,3)asdfa"), 13)

    # sumValidMulWithSwitches -- but no switches

    def testSumValidMulWithSwitchesSimgle(self):
        self.assertEqual(sumValidMulWithSwitches("mul(2,2)"), 4)

    def testSumvalidMulsWithSwitchesSingleWithJunk(self):
        self.assertEqual(sumValidMulWithSwitches("adfamul(2,2)adf"), 4)

    def testSumValidMulsWithSwitchesMultiple(self):
        self.assertEqual(sumValidMulWithSwitches("mul(2,2)mul(3,3)"), 13)

    def testSumValidMulsWithSwitchesMultipleWithJunk(self):
        self.assertEqual(sumValidMulWithSwitches("33amul(2,2)asdmul(3,3)asdfa"), 13)

    # sumValidMulWithSwitches -- with switches
    def testWithSwitchesStartDoNoDont(self):
        self.assertEqual(sumValidMulWithSwitches("do()mul(2,2)mul(3,3)"), 13)

    def testWithSwitchesAllContained(self):
        self.assertEqual(sumValidMulWithSwitches("do()mul(2,2)mul(3,3)don't()"), 13)

    def testWithSwitchesNoDoEndDont(self):
        self.assertEqual(sumValidMulWithSwitches("mul(2,2)mul(3,3)don't()"), 13)

    def testWithSwitchesStartNoDoThenContained(self):
        self.assertEqual(sumValidMulWithSwitches("mul(1,1)do()mul(2,2)mul(3,3)don't()"), 14)

    def testWithSwitchesStartWithDontMiddleDo(self):
        self.assertEqual(sumValidMulWithSwitches("don't()mul(1,1)do()mul(2,2)mul(3,3)don't()"), 13)

    def testWithSwitchesStartWithDontNoDo(self):
        self.assertEqual(sumValidMulWithSwitches("don't()mul(1,1)mul(2,2)mul(3,3)don't()"), 0)
    
    def testWithSwitchesMultipleDo(self):
        self.assertEqual(sumValidMulWithSwitches("do()mul(1,1)do()mul(2,2)mul(3,3)don't()"), 14)

    def testWithSwitchesMultipleValidSections(self):
        self.assertEqual(sumValidMulWithSwitches("don't()mul(1,1)do()mul(2,2)mul(3,3)don't()mul(5,5)mul(6,6)do()mul(2,2)mul(2,1)"), 19)

if __name__ == '__main__':
    unittest.main()
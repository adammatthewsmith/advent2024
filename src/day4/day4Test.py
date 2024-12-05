import unittest
from .day4 import countXMas, countXmas, hasSlopeDownX, hasSlopeUpX

class Day4UnitTest(unittest.TestCase):
    # Slope detection single
    def testSlopeUpForward(self):
        input = ["..S",
                 ".A.",
                 "M.."]
        self.assertEqual(hasSlopeUpX(input, 1, 1), True)

    def testSlopeUpBackward(self):
        input = ["..M",
                 ".A.",
                 "S.."]
        self.assertEqual(hasSlopeUpX(input, 1, 1), True)
       
    def testSlopeDownForward(self):
        input = ["M..",
                 ".A.",
                 "..S"]
        self.assertEqual(hasSlopeDownX(input, 1, 1), True)
        
    def testSlopeDownBackward(self):
        input = ["S..",
                 ".A.",
                 "..M"]
        self.assertEqual(hasSlopeDownX(input, 1, 1), True)

    # Slope Detection with X
    def testXBothForward(self):
        input = ["M.S",
                 ".A..",
                 "M.S"]
        
        self.assertEqual(hasSlopeUpX(input, 1, 1), True)
        self.assertEqual(hasSlopeDownX(input, 1, 1), True)

    def testXUpReversed(self):
        input = ["M.M",
                 ".A..",
                 "S.S"]
        
        self.assertEqual(hasSlopeUpX(input, 1, 1), True)
        self.assertEqual(hasSlopeDownX(input, 1, 1), True)
    
    def testXDownReversed(self):
        input = ["S.S",
                 ".A..",
                 "M.M"]
        
        self.assertEqual(hasSlopeUpX(input, 1, 1), True)
        self.assertEqual(hasSlopeDownX(input, 1, 1), True)

    def testXBothReversed(self):
        input = ["S.M",
                 ".A..",
                 "S.M"]
        
        self.assertEqual(hasSlopeUpX(input, 1, 1), True)
        self.assertEqual(hasSlopeDownX(input, 1, 1), True)

    # -- 
    def testCountXBothForward(self):
        input = ["M.S",
                 ".A.",
                 "M.S"]
        
        self.assertEqual(countXMas(input), 1)

    def testCountXUpReversed(self):
        input = ["M.M",
                 ".A.",
                 "S.S"]
        
        self.assertEqual(countXMas(input), 1)

    def testCountXDownReversed(self):
        input = ["S.S",
                 ".A.",
                 "M.M"]
        
        self.assertEqual(countXMas(input), 1)

    def testCountXBothReversed(self):
        input = ["S.M",
                 ".A.",
                 "S.M"]
        
        self.assertEqual(countXMas(input), 1)

     # x-mas sample
    def testWithProvidedInput(self):
        input = [".M.S......",
                 "..A..MSMS.",
                 ".M.S.MAA..",
                 "..A.ASMSM.",
                 ".M.S.M....",
                 "..........",
                 "S.S.S.S.S.",
                 ".A.A.A.A..",
                 "M.M.M.M.M.",
                 ".........."]
        
        self.assertEqual(countXMas(input), 9)

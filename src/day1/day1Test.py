import unittest
from .day1 import calcDiffScore, calcSimScore, readLists

class Day1UnitTest(unittest.TestCase):
    def testReadLists(self):
        testfile = "src/day1/test1.txt"
        [leftList, rightList] = readLists(testfile)
        self.assertEqual(leftList, [1, 2, 3, 3, 3, 4])
        self.assertEqual(rightList, [3, 3, 3, 4, 5, 9])

    def testDiffScoreSampleInput(self):
        self.assertEqual(calcDiffScore([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9]), 11)

    def testDiffScoreSameList(self):
        self.assertEqual(calcDiffScore([1, 2, 3, 4], [1, 2, 3, 4]), 0)

    def testSimScoreSampleInput(self):
        self.assertEqual(calcSimScore([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5, 9]), 31)

    def testSimScoreAll1s(self):
        self.assertEqual(calcSimScore([1, 1, 1], [1, 1, 1]), 9)
    
    def testSimScoreSameList(self):
        self.assertEqual(calcSimScore([1, 2, 3], [1, 2, 3]), 6)


if __name__ == '__main__':
    unittest.main()
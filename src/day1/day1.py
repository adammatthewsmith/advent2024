import sys
from typing import List
from bisect import bisect_left, bisect_right

"""
Convenience function for reading two tab separated lists from a file,
sorting them, and returning the lists in a tuple. 

Assumptions 
 - only ints
 - equal sized lists
 - correctly formatted tab separation
"""
def readLists(filename) -> tuple[List[int], List[int]]:
    leftList: List[int] = []
    rightList: List[int] = []

    with open(filename) as file:
        for line in file:
            split = line.rstrip().split()
            leftList.append(int(split[0]))
            rightList.append(int(split[1]))

    leftList.sort()
    rightList.sort()

    return leftList, rightList

"""
Given two sorted lists of integers, calculate the "difference score" by
summing the differences between the items at the same index in each list.
"""
def calcDiffScore(leftList: List[int], rightList: List[int]) -> int:
    diff: int = 0

    for i in range(len(leftList)):
        leftItem = leftList[i]
        rightItem = rightList[i]

        diff += abs(leftItem - rightItem)

    return diff


"""
Given two sorted lists of integers, calculate the "similarity score" by 
summing the multiplication of each item in the left list by the number
of times that item appears in the right list.
"""
def calcSimScore(leftList: List[int], rightList: List[int]) -> int:
    simScore: int = 0

    for item in leftList:
        leftIndex = bisect_left(rightList, item)

        if (leftIndex < len(rightList) and rightList[leftIndex] == item):
            # The list contains the item. Find out how many and add the score. 
            rightIndex = bisect_right(rightList, item)
            count: int = rightIndex - leftIndex

            simScore += (item * count)


    return simScore

"""
Read in the file provided as the first argument. 
"""
if __name__ == "__main__":
    filename: str = sys.argv[1]

    [leftList, rightList] = readLists(filename)

    print(f"Difference Score: {calcDiffScore(leftList, rightList)}")
    print(f"Similarity Score: {calcSimScore(leftList, rightList)}")
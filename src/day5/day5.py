import math
import re
import sys

from typing import List, Optional, Self, Tuple, Dict, Set

class Day5Puzzle:
    def __init__(self, orderPairs: List[Tuple[str, str]], pagesList: List[List[str]]):
        # Set locals
        self.orderPairs = orderPairs
        self.pagesList = pagesList
        self.ancestorMap: Dict[str, Set[str]] = {}
        self.badOrders: List[str] = []
        self.goodSum = 0
        self.badSum = 0

        # Build the data structure
        for pair in orderPairs:
            if pair[1] not in self.ancestorMap:
                self.ancestorMap[pair[1]] = set() 
            self.ancestorMap[pair[1]].add(pair[0])

    def str(self):
        return f"orders: {self.orderPairs}\npageLists: {self.pagesList}"

    def evaluateOrder(self, pages: List[str]) -> bool:
        altered = False

        for firstPageIndex in range(len(pages)):
            for secondPageIndex in range(firstPageIndex + 1, len(pages)):
                firstPageValue = pages[firstPageIndex]
                secondPageValue = pages[secondPageIndex]

                if firstPageValue in self.ancestorMap and secondPageValue in self.ancestorMap.get(firstPageValue):
                    #print(f"{pages} is bad because {firstPageValue} cannot come before {secondPageValue}")
                    altered = True
                    #print(f"\tputting {pages[secondPageIndex]} before {pages[firstPageIndex]}")

                    pages.insert(firstPageIndex, pages[secondPageIndex])
                    del pages[secondPageIndex + 1]

                    # Reset the loop counters so that original firstPageIndex outer loop is restarted
                    # Set the secondPageIndex to the firstPageIndex so that the next iteration
                    # of the inner loop starts at the next index.
                    secondPageIndex = firstPageIndex
                    
        if altered:
            self.badSum += int(pages[math.trunc(len(pages)/2)])            
        else:
            self.goodSum += int(pages[math.trunc(len(pages)/2)])        

    def doIt(self) -> int:
        # Check the pages.
        for pages in self.pagesList:
            self.evaluateOrder(pages)

        print(f"part1: {self.goodSum}")
        print(f"part2: {self.badSum}")

def readPuzzle(filename) -> Day5Puzzle:
    orders: List[Tuple[str, str]] = []
    pageLists: List[List[str]] = []

    with open(filename) as file:
        for line in file:

            if re.match(r"\d+\|\d+", line.strip()):
                orders.append(tuple(line.strip().split("|")))
            
            elif line.strip() != "":
                pageLists.append(line.strip().split(","))
            
    return Day5Puzzle(orders, pageLists)

if __name__ == "__main__":
    filename: str = sys.argv[1]

    puzzle = readPuzzle(filename)

    puzzle.doIt()
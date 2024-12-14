import math
import re
import sys

from typing import List, Optional, Self, Tuple, Dict, Set

# This file was my first attempt when I thought the page ordering was transitive. 
# It builds a list of trees of dependency chains, and then traverses it for a fast
# lookup of all ancestors of any node.

class Node:
    def __init__(self, value: str):
        self.value: str = value
        self.parents: List[Self] = []
        self.ancestorSet: Optional[Set] = None
    
class TreeMap():
    def __init__(self):
        self.items: Dict[str, Node] = {}

    def insert(self, parent: str, child: str):
        parentNode = self.items.get(parent) if parent in self.items else Node(parent)
        childNode = self.items.get(child) if child in self.items else Node(child)

        self.items[parent] = parentNode
        self.items[child] = childNode

        childNode.parents.append(parentNode)

    def str(self) -> str:
        return [str(node) for node in self.items]
    
        
"""
For each node in the list, update the full set of its ancestors, and return the full set of ancestors for 
all of the nodes.
"""
def updateAnsestors(nodes: list[Node]) -> Set[str]:
    fullAncestors = set();
    
    for node in nodes:
        print(f"Processing {node.value}")

        fullAncestors.add(node.value)

        # If the node has parents, and the ancestor set has not been calculated then calculate it 
        # recursively
        if node.ancestorSet == None:
            # Hack for "seen". There are cycles in the dependencies, but I think 
            # this is ok because not all pages have to appear in the updates. 
            # There is definitely a cycle where 91->48->11->35->91. 
            # By short-circuiting the duplicate updateAncestor calls, 91 will still
            # be in its own ancestor set but we won't calculate it more than once 
            node.ancestorSet = set()
            node.ancestorSet = updateAnsestors(node.parents)
            
        # Update the full set for the provided list of nodes
        fullAncestors.update(node.ancestorSet)

    return fullAncestors

class Day5Puzzle:
    def __init__(self, orderPairs: List[Tuple[str, str]], pagesList: List[List[str]]):
        # Set locals
        self.orderPairs = orderPairs
        self.pagesList = pagesList
        self.ancestorTreeMap = TreeMap()
        self.goodSum = 0

        # Build the data structure
        for pair in orderPairs:
            self.ancestorTreeMap.insert(parent=pair[0], child=pair[1])
        
        # Calculate the ancestors
        updateAnsestors(list(self.ancestorTreeMap.items.values()))


    def str(self):
        return f"orders: {self.orderPairs}\npageLists: {self.pagesList}"

    def evaluateOrder(self, pages: List[str]):
        for firstPageIndex in range(len(pages)):
            for secondPageIndex in range(firstPageIndex + 1, len(pages)):
                firstPageNode = self.ancestorTreeMap.items.get(pages[firstPageIndex])
                secondPageNode = self.ancestorTreeMap.items.get(pages[secondPageIndex])

                if secondPageNode.value in firstPageNode.ancestorSet:
                    print(f"{pages} bad because {firstPageNode.value} cannot come before {secondPageNode.value}")
                    return False
        
        return True

    def part1(self) -> int:
        sumOfMiddles = 0

        # Check the pages.
        for pages in self.pagesList:
            if self.evaluateOrder(pages):
                sumOfMiddles += int(pages[math.trunc(len(pages)/2)])

        return sumOfMiddles          

"""
"""
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

"""
We have the dependencies between two numbers.
We have the attempts that need to be verified. 

We can build a tree (or list of trees) of dependencies. 

With this we could easily build _a_ viable path given a list of pages, but we need to verify that a given path is valid. 

The final check will need to be 
For each list of page order, 
    For each page
        check that none of the subsequent items in the list appear in the parent hierarchy for the current item.
Ths is already (n^2)*m where n is the length of the lists, and m is the number of lists, so the check needs to be fast. ideally, 
it's a set for each number that includes the full parent hierarchy for that number. 


build it
    iterate through the pairs and build the tree of dependencies.

    Iterate through the tree depth first. recursively build the set at each node by calculating the set for each dependency and returning that plus self.value.

1 | 2
2 | 3

3 (2,1) -> 2 (1) -> 1

3 : single digit is a base case, but this should be a 'good' list because nothing is out of order. 
1, 2 : second page is not in first page's dependencies: good
2, 1 : second page (1) is in first page's (2) dependencies: bad
2, 4, 1 : 2, 4 is good (4 not in 2 deps), 2, 1 is bad
"""

if __name__ == "__main__":
    filename: str = sys.argv[1]

    puzzle = readPuzzle(filename)

    print(f"Puzzle: {puzzle.str()}")
    print(f"Part 1: {puzzle.part1()}")

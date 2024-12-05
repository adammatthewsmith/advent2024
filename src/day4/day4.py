import sys
from typing import List

"""
Read the day4 puzzle string and return a matrix of characters.
"""
def readPuzzle(filename) -> List[List[str]]:
    puzzle: List[List[str]] = []

    with open(filename) as file:
        for line in file:
            puzzle.append(list(line.strip()))
            
    return puzzle

"""
Part 1
"""
def countXmas(puzzle: List[List[str]]):
    xmasCount: int = 0

    for row in range(len(puzzle)):
        for column in range(len(puzzle[row])):
            start = puzzle[row][column]

            if start == 'X':
                # look up
                if row >= 3 and puzzle[row-1][column] == 'M' and puzzle[row-2][column] == 'A' and puzzle[row-3][column] == 'S':
                    xmasCount += 1

                # look down
                if row + 4 <= len(puzzle) and puzzle[row+1][column] == 'M' and puzzle[row+2][column] == 'A' and puzzle[row+3][column] == 'S':
                    xmasCount += 1

                # look left
                if column >=3 and puzzle[row][column-1] == 'M' and puzzle[row][column-2] == 'A' and puzzle[row][column-3] == 'S':
                    xmasCount += 1
                
                # look right
                if column + 4 <= len(puzzle[row]) and puzzle[row][column+1] == 'M' and puzzle[row][column+2] == 'A' and puzzle[row][column+3] == 'S':
                    xmasCount += 1
                
                # look up-left
                if row >= 3 and column >=3 and puzzle[row-1][column-1] == 'M' and puzzle[row-2][column-2] == 'A' and puzzle[row-3][column-3] == 'S':
                    xmasCount += 1

                # look up-right
                if row >= 3 and column + 4 <= len(puzzle[row]) and puzzle[row-1][column+1] == 'M' and puzzle[row-2][column+2] == 'A' and puzzle[row-3][column+3] == 'S':
                    xmasCount += 1
                    
                # look down-left
                if row + 4 <= len(puzzle) and column >=3 and puzzle[row+1][column-1] == 'M' and puzzle[row+2][column-2] == 'A' and puzzle[row+3][column-3] == 'S':
                    xmasCount += 1

                # look down-right
                if row + 4 <= len(puzzle) and column + 4 <= len(puzzle[row]) and puzzle[row+1][column+1] == 'M' and puzzle[row+2][column+2] == 'A' and puzzle[row+3][column+3] == 'S':
                    xmasCount += 1

    return xmasCount

"""
Check for 
M..
.A.
..S

or 

S..
.A.
..M
"""
def hasSlopeDownX(puzzle: List[List[int]], row: int, col:int):
    # Check top left to lower right
    return (puzzle[row-1][col-1] == 'M' and puzzle[row+1][col+1] == 'S') or (puzzle[row-1][col-1] == 'S' and puzzle[row+1][col+1] == 'M')

"""
Check for 
..S
.A.
M..

or 

..M
.A.
S..
"""
def hasSlopeUpX(puzzle: List[List[int]], row: int, col:int):
    # Check lower left to top left
    return (puzzle[row+1][col-1] == 'M' and puzzle[row-1][col+1] == 'S') or (puzzle[row+1][col-1] == 'S' and puzzle[row-1][col+1] == 'M')

"""
Part 2
"""
def countXMas(puzzle: List[List[str]]):
    xmasCount: int = 0

    # Iterate through the matrix, skipping the first and last row and first and last column since
    # the A we are looking for must not be on the border in order to have room for the X.
    for row in range(1, len(puzzle) - 1):
        for column in range(1, len(puzzle[row]) - 1):
            start = puzzle[row][column]

            if start == 'A':
                if (hasSlopeDownX(puzzle, row, column) and hasSlopeUpX(puzzle, row, column)):
                    xmasCount += 1

    return xmasCount

if __name__ == "__main__":
    filename: str = sys.argv[1]

    puzzle = readPuzzle(filename)

    print(f"XMAS Occurences: {countXmas(puzzle)}")
    print(f"X-MAS Occurences: {countXMas(puzzle)}")
import re
import sys
from typing import List

def readProgram(filename) -> str:
    with open(filename) as file:
        return file.read()

"""
Given a well formatted multiplication string "mul(x, y)", multiple x * y and return the result.
"""
def doMul(mulString: str) -> int:
    nums = re.findall(r"\d{1,3}", mulString)

    assert len(nums) == 2

    return int(nums[0]) * int(nums[1])

"""
Given a string that contains well formated multiplication strings and other characters,
extract the multiplicaiton strings, perform the multiplication, and sum the results.
"""
def sumValidMuls(program: str) -> int:
    muls = re.findall(r'mul\(\d{1,3},\s?\d{1,3}\)', program)
    sumOfMuls = sum([doMul(mul) for mul in muls])

    return sumOfMuls

"""
Given a string that contains well formatted multiplication strings, other characters, and
do() and don't() token, multiply all mul strings and sum iff they are at the beginning of 
the program or most recently after a do() token. 
"""
def sumValidMulWithSwitches(program: str) -> int:
    doSegments: List[str] = []
    
    # Process the program in chunks defined by do() and don't() delimeters.
    # Remove chunks from the program as they are processed.
    # The loop _should_ leave the program string always starting with either
    # valid text for mul detection, or a don't()
    while len(program) > 0:
        # If there are no don't()s then all of program is 
        # enabled. Add it to the segments and clear it.
        doNotMatch = re.search(r"don't\(\)", program)
        if doNotMatch == None:
            doSegments.append(program)
            program = ""
        
        # If there is a don't() 
        else:
            # Add the good part (from the beginning to the start of the don't) to doSegments
            doSegments.append(program[:doNotMatch.start()])
            # Remove from program the part of the string that was added to doSegments  
            program = program[doNotMatch.start():]
            # Look for a do(). The only way for more valid muls after a don't() is if there is a do()
            doMatch = re.search(r"do\(\)", program)
            # If there is a do(), then use its end index as the new start of the program.
            # If there is no do(), then there are no possible valid muls left
            program = "" if doMatch == None else program[doMatch.end():]

    return sum([sumValidMuls(segment) for segment in doSegments])

if __name__ == "__main__":
    filename = sys.argv[1]
    program = readProgram(filename)

    print(f"Sum of valid muls: {sumValidMuls(program)}")
    print(f"Sum of enabled muls: {sumValidMulWithSwitches(program)}")
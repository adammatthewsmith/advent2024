import sys
from typing import List
from bisect import bisect_left, bisect_right

"""
Reads in the matrix of reports. Each line should be a white space delimited row of ints.
"""
def readReports(filename) -> List[List[int]]:
    with open(filename) as file:
        return [[int(level) for level in report.split()] for report in file]

"""
Determine if a single report (list of ints) is safe according to the problem definition.
"""
def isReportSafe(report: List[int]) -> bool:
    decreasing: bool = None

    for i in range(1, len(report)):
        level: int = report[i]
        prevLevel: int = report[i-1]
        diff: int = abs(level - prevLevel)
        
        if (diff < 1 or diff > 3):
            return False

        localDecreasing: bool = False if level - prevLevel > 0 else True

        if (decreasing == None):
            decreasing = localDecreasing
            continue

        if (decreasing != localDecreasing):
            return False
    
    return True

"""
Determine if a single report (list of ints) is safe according to the problem definition
when the "dampener" is used. If the whole report is unsafe then iteratively check the list
with 1 item removed until the whole list is tested (return false) or a safe dampened report
is found.
"""
def isReportSafeWithDampener(report: List[int]):
    if (isReportSafe(report)):
        return True
    else:
        for i in range(len(report)):
            if (isReportSafe(report[:i] + report[i+1:])):
                return True
        
        return False

"""
Counts the safe reports (part 1)
"""
def countSafeReports(reports: List[List[int]]) -> int:
    safeReports: int = 0

    for report in reports:
        safeReports += 1 if isReportSafe(report) else 0
            
    return safeReports

"""
Counts the safe reports with the dampener. 
"""
def countSafeReportsWithDampener(reports: List[List[int]]) -> int:
    safeReports: int = 0

    for report in reports:
        safeReports += 1 if isReportSafeWithDampener(report) else 0
            
    return safeReports

"""
Read the file and calculate the safe reports.
"""
if __name__ == "__main__":
    filename: str = sys.argv[1]

    reports = readReports(filename)

    print(f"Safe Reports: {countSafeReports(reports)}")
    print(f"Safe Reports With Dampener: {countSafeReportsWithDampener(reports)}")
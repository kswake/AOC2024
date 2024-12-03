import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "puzzle2input.txt")

with open(file_path, "r") as reportsMaster:
    reports = reportsMaster.readlines()

def diffTest(levels):
    diffTestPass = True
    for i in range(len(levels)-1):
        currDiff = abs((int(levels[i+1]) - int((levels[i]))))
        if currDiff < 1 or currDiff > 3:
            diffTestPass = False
    return diffTestPass

def isIncreasingOnly(levels):
    increasingOnly = True
    for i in range(len(levels)-1):
        if int(levels[i+1]) <= int(levels[i]):
            increasingOnly = False
            break
    return increasingOnly

def isDecreasingOnly(levels):
    decreasingOnly = True
    for i in range(len(levels)-1):
        if int(levels[i+1]) >= int(levels[i]):
            decreasingOnly = False
            break
    return decreasingOnly

safeCount = 0
counter = 0

for item in reports:
    counter = counter+1
    currLevels = [int(x) for x in item.strip().split()]
    if (diffTest(currLevels)==True):
        if isIncreasingOnly(currLevels)==True:
            safeCount = safeCount + 1
        elif isDecreasingOnly(currLevels)==True:
            safeCount = safeCount + 1

print(safeCount)

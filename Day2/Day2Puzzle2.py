import os

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "puzzle2input.txt")

with open(file_path, "r") as reportsMaster:
    reports = reportsMaster.readlines()

safeCount = 0

def is_safe_report(levels):
    diffs = [int(levels[i+1]) - int(levels[i]) for i in range(len(levels)-1)]

    if any(d == 0 for d in diffs):
        return False
    
    increasing = all(d > 0 for d in diffs)
    decreasing = all(d < 0 for d in diffs)

    if not (increasing or decreasing):
        return False
    
    if any(abs(d) < 1 or abs(d) > 3 for d in diffs):
        return False
    
    return True

def is_safe_report_pd(levels):
    for i in range (len(levels)):
        newLevels = levels[:i] + levels[i+1:]
        if is_safe_report(newLevels) == True:
            return True
    
    return False

for item in reports:
    currLevels = item.split()
    if is_safe_report(currLevels) == True:
        safeCount+=1
    elif is_safe_report_pd(currLevels) == True:
        safeCount+=1

print(safeCount)
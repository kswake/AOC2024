import os

script_directory = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_directory, "locationList.txt")

with open(file_path, "r") as locationList:
    lines = locationList.readlines()
    numPairs = len(lines)


listA = []
listB = []

for i in range (numPairs):
    currPair = lines[i].split()
    listA.append(currPair[0])
    listB.append(currPair[1])

simScore = 0

for i in range (numPairs):
    simScore = simScore + ( int(listA[i]) * listB.count(listA[i]) )

print(simScore)
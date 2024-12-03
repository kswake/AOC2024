
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

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as pivot
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

listA = quicksort(listA)
listB = quicksort(listB)

sumDiff = 0

for i in range(numPairs):
    currDiff = abs(int(listA[i])-int(listB[i]))
    sumDiff = sumDiff+currDiff

print(sumDiff)
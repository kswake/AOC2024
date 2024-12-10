### this code isn't currently outputting the correct answer, need to revisit it

import os
from itertools import cycle

idNum, fsChk, sparseMap = 0, 1, []
with open (os.path.join(os.path.dirname(os.path.abspath(__file__)),"d9input.txt"),'r') as denseMap:
    for num in denseMap.read():
        if fsChk%2 != 0:
            for i in range(int(num)):
                sparseMap.append(idNum)
            idNum+=1
        else:
            for j in range(int(num)):
                sparseMap.append(".")
        fsChk+=1

reverseNums =[]
dotcount=0
sparse_reversed = list(reversed(sparseMap))
for x in sparse_reversed:
    if x != ".":
        reverseNums.append(x)
    else:
        dotcount+=1
revCycle = cycle(reverseNums)

for loc in range(len(sparseMap)):
    if loc < dotcount:
        if sparseMap[loc] == ".":
            sparseMap[loc] = next(revCycle)

finalMap = []
for i in range(len(sparseMap)):
    if sparseMap[i] == ".":
        break
    else:
        finalMap.append(sparseMap[i])

checkSum = 0
for z in range(len(finalMap)):
    checkSum += z * finalMap[z]

print(checkSum)
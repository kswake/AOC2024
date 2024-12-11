import os

#load dense file into sparse format
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

#reorg sparse format
endpoint = len(sparseMap)-1
for i in range(len(sparseMap)):
    if sparseMap[i] == ".":
        for j in range(endpoint, i, -1):
            if sparseMap[j] != ".":
                sparseMap[i] = sparseMap[j]
                sparseMap[j] = "."
                endpoint = j
                break
    if i>=endpoint:
        break

checksum=0
for x in range(len(sparseMap)):
    if sparseMap[x] == ".":
        break
    else:
        checksum+=x*sparseMap[x]

print(checksum)
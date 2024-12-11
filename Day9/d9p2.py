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

def find_next_contig_space(startPos, endPos, reqSize):
    currGap = []
    for i in range(startPos,endPos):
        if sparseMap[i] == ".":
            currGap.append(i)
        elif sparseMap[i] != ".":
            currGap = []
        if len(currGap) == reqSize:
            return currGap

#reorg sparse format    
index = 0
for i in range(len(sparseMap)-1,-1,-1):
    if sparseMap[i] != ".":
        currNum = [d for d in str(sparseMap[i])]

        gapPos = find_next_contig_space(0,i,len(currNum))
        if gapPos is not None:
            #index += gapPos[len(currNum)-1]
            for p in range(len(gapPos)):
                sparseMap[gapPos[p]]=currNum[p]
                sparseMap[i] = "."
            print(str(i) + " " + str(gapPos[len(currNum)-1]))

        
#dump sparsemap
with open (os.path.join(os.path.dirname(os.path.abspath(__file__)),"d9dumpfile.txt"),'w') as output:
    for line in sparseMap:
        output.write(str(line)+",")

#calculate checksum
checksum=0
for x in range(len(sparseMap)):
    if sparseMap[x] == ".":
        continue
    else:
        checksum += x * int(sparseMap[x])

print(checksum)
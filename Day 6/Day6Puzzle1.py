import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"puzzleInput6test.txt")

with open (file_path, "r") as mapInput:
    mapMaster = mapInput.read().splitlines()

directions = ["^",">","v","<"]

def get_pos(map): #done - returns [row,col]
    row=0
    for line in map:
        row+=1
        for col in range(len(line)):
            if line[col] in directions:
                return[row-1,col]
            
def get_direction(line): #done - returns "^", ">" etc. (str)
    for position in line:
        if position in directions:
            return position

def turn_right(currDirection): #done - returns new direction flipped 90deg: "^" -> ">" etc.
    if directions.index(currDirection) == 3:
        return(str(directions[0]))
    else:
        return directions[(directions.index(currDirection)+1)]

def find_new_pos(oldPos): #done - returns [x,y] of new location
    row,col = oldPos[0],oldPos[1]
    direction = get_direction(mapMaster[row])

    if direction == ">":
        travelPath = mapMaster[row].split(">",1)[1]
        offset = 0
        for loc in travelPath:
            if loc == "#":
                return [row,col+offset]
            offset+=1
        return[-1,-1]
    
    elif direction == "<":
        travelPath = mapMaster[row].split("<",1)[0]
        offset = 0
        for loc in reversed(travelPath):
            if loc == "#":
                return [row,col-offset]
            offset+=1
        return[-1,-1]

    elif direction == "^":
        travelPath = []
        for preRow in range(0,row):
            travelPath.append(mapMaster[preRow][col])
        offset = 0
        for loc in reversed(travelPath):
            if loc == "#":
                return [row-offset,col]
            offset+=1    
        return[-1,-1]
    
    elif direction == "v":
        travelPath = []
        for folRow in range(row,(len(mapMaster)-1)):
            travelPath.append(mapMaster[folRow][col])
        offset = 0
        for loc in travelPath:
            if loc == "#":
                return [row+offset,col]
            offset+=1    
        return[-1,-1]

def move_pointer(moveFrom, moveTo, currMap): #think this works
    oldFromLine = currMap[moveFrom[0]]
    currDir = get_direction(oldFromLine)
    newFromLine = (oldFromLine.split(currDir)[0] + "." + oldFromLine.split(currDir)[1])
    oldToLine = currMap[moveTo[0]]
    newToLine = (oldToLine[:moveTo[1]] + turn_right(currDir) + oldToLine[moveTo[1]+1:])

    currMap[moveFrom[0]] = newFromLine
    currMap[moveTo[0]] = newToLine
    return currMap

moves = 0

currPos = get_pos(mapMaster)
currMap = mapMaster

while currPos != [-1,-1]:
    move_pointer(get_pos(currMap), find_new_pos(get_pos(currMap)), currMap)
    currPos = get_pos(currMap)


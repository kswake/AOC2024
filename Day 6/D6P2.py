import os

with open (os.path.join(os.path.dirname(os.path.abspath(__file__)),"puzzleInput6.txt"), "r") as input:
    mapState = [list (pos) for pos in input.read().splitlines()]    

directions = ["^",">","v","<"]
inf_loop_locs = []

def write_map_state(map): #only used for dumping state to drive
    with open (os.path.join(os.path.dirname(os.path.abspath(__file__)),"puzzle6DataDump.txt"), "w") as dumpFile:
        for line in map:
            for char in line:
                dumpFile.write(char)
            dumpFile.write('\n')

def find_curr_pos(map): #returns [x,y] position of the guard on a given map state
    for r in range(len(map)):
        for c in range(len(map[r])):
            if map[r][c] in directions:
                return [r,c]

def find_next_pos(map): #returns [x,y] of next square or [-999,-999] if next square would be out of bounds
    guardPos = find_curr_pos(map)
    guardDir = map[guardPos[0]][guardPos[1]]
    if guardDir == "^":
        nextPos = [guardPos[0]-1,guardPos[1]]
    if guardDir == ">":
        nextPos = [guardPos[0],guardPos[1]+1]
    if guardDir == "v":
        nextPos = [guardPos[0]+1,guardPos[1]]
    if guardDir == "<":
        nextPos = [guardPos[0],guardPos[1]-1]
    if -1 in nextPos or 130 in nextPos:
        return [-999,-999]
    else:
        return nextPos 
    
def rotate_right(map): #returns the map state with a right-rotated guard (e.g. IN: "^" -> OUT: ">")
    currPos = find_curr_pos(map)
    guard = map[currPos[0]][currPos[1]]
    if directions.index(guard)==3:
        map[currPos[0]][currPos[1]] = directions[0]
    else: 
        map[currPos[0]][currPos[1]] = directions[directions.index(guard)+1]
    return map

    movesCount = 1
    for row in map:
        for location in row:
            if location == "X":
                movesCount+=1
    return movesCount

def move(map): #alters given map state according to rules, returns new map state as list
    currPos = find_curr_pos(map)
    nextPos = find_next_pos(map)
    
    nextContents = map[nextPos[0]][nextPos[1]]

    if nextContents == "." or nextContents == "X":
        map[nextPos[0]][nextPos[1]] = map[currPos[0]][currPos[1]]
        map[currPos[0]][currPos[1]] = "X"
    if nextContents == "#":
        map = rotate_right(map)
    return map

def find_infloop(localMap):
    
    #add current postion and direction to list of moved positions and directions
    startPos = find_curr_pos(localMap)
    prevLocDirs = [startPos[0], startPos[1], localMap[startPos[0]][startPos[1]]]
    
    #place the obstacle
    obsPos = find_next_pos(localMap)
    localMap[obsPos[0]][obsPos[1]] = "#"

    while find_next_pos(localMap) != [-999,-999]:
        currPos = find_curr_pos(localMap)
        currLocDir = [currPos[0], currPos[1], localMap[currPos[0]][currPos[1]]]
        print(currLocDir)
        print(prevLocDirs)
        if currLocDir in prevLocDirs:
            return obsPos
        prevLocDirs.append(currLocDir)
    return []

while find_next_pos(mapState) != [-999,-999]: 
    move(mapState)
    localMap = mapState
    print(find_infloop(localMap))
import os

with open (os.path.join(os.path.dirname(os.path.abspath(__file__)),"trailmap.txt"),'r') as input:
    trailmap = []
    for item in input: trailmap.append(list(item.strip()))
map_size = len(trailmap)-1

def get_trailhead_coords(map):
    th = []
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == "0":
                th.append(list([str(row),str(col)]))
    return th

def get_next_steps(x,y,searchInt):
    validNextSteps = []
    for coordOffset in [[-1,0],[0,1],[1,0],[0,-1]]:
        if not (int(x)+int(coordOffset[0]) < 0 or int(x)+int(coordOffset[0]) > int(map_size) or int(y)+int(coordOffset[1]) < 0 or int(y)+int(coordOffset[1]) > int(map_size)):
            if int(trailmap[int(x)+int(coordOffset[0])][int(y)+int(coordOffset[1])]) == int(searchInt)+1:
                validNextSteps.append([int(x)+int(coordOffset[0]),int(y)+int(coordOffset[1]),searchInt+1])
    return validNextSteps

def get_reachable_9s(th_x,th_y):

    nextPaths = get_next_steps(th_x,th_y,0)

    for height in range(1,9):
        newPaths = []
        for path in nextPaths:
            addSteps = get_next_steps(path[0],path[1],height)
            for step in addSteps:
                if step not in newPaths:
                    newPaths.append(step)
            nextPaths = newPaths

    uniquePaths = {tuple(path[:2]) for path in nextPaths}
    
    return(len(uniquePaths))

runningTotal9s = 0
for trailhead in get_trailhead_coords(trailmap):
    runningTotal9s += get_reachable_9s(trailhead[0],trailhead[1])
print(runningTotal9s)
import os, math
with open (os.path.join(os.path.dirname(os.path.abspath(__file__)),"d8input.txt"),'r') as input:
    topologyGrid =[]
    for item in input: topologyGrid.append(list(item.strip()))
bounds=[0,len(topologyGrid)-1]

def get_antenna_list(topologyGrid): 
    antenna_list = []
    for x in range(len(topologyGrid)):
        for y in range(len(topologyGrid[x])):
            if topologyGrid[x][y] != ".":
                antenna_list.append([topologyGrid[x][y],x,y])
    return(antenna_list)

def get_like_antenna_pos(anType,x,y,antennaList):
    likeAntennas = []
    for antenna in antennaList:
        if antenna[0] == anType and (antenna[1]!=x and antenna[2]!=y):
            likeAntennas.append([antenna[1],antenna[2]])
    return likeAntennas

def get_antinodes(antenna):
    antinodes = []
    curr_x, curr_y = antenna[1], antenna[2]
    likeAntennas = get_like_antenna_pos(antenna[0], curr_x, curr_y, allAntennas)
    
    for likeAnt in likeAntennas:
        x_diff = likeAnt[0] - curr_x
        y_diff = likeAnt[1] - curr_y

        g = math.gcd(x_diff, y_diff)
        step_x = x_diff // g
        step_y = y_diff // g
        
        test_x = curr_x
        test_y = curr_y
        while 0 <= test_x <= bounds[1] and 0 <= test_y <= bounds[1]:
            antinodes.append([test_x, test_y])
            test_x += step_x
            test_y += step_y
        
        test_x = curr_x - step_x
        test_y = curr_y - step_y
        while 0 <= test_x <= bounds[1] and 0 <= test_y <= bounds[1]:
            antinodes.append([test_x, test_y])
            test_x -= step_x
            test_y -= step_y
    return (antinodes)

allAntennas = get_antenna_list(topologyGrid)
allAntinodes = []
for antenna in allAntennas:
    antinodes = get_antinodes(antenna)
    for an in antinodes:
        if an not in allAntinodes:
            allAntinodes.append(an)
print(len(allAntinodes))
import os
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
    curr_x,curr_y = antenna[1],antenna[2]
    likeAntennas = get_like_antenna_pos(antenna[0],antenna[1],antenna[2],allAntennas)
    for likeAnt in likeAntennas:
        antinode_x = likeAnt[0] + (likeAnt[0] - curr_x)
        antinode_y = likeAnt[1] + (likeAnt[1] - curr_y)
        if not (antinode_x < bounds[0] or antinode_y < bounds[0] or antinode_x > bounds[1] or antinode_y > bounds[1]):
            antinodes.append([antinode_x,antinode_y])
    return(antinodes)

allAntennas = get_antenna_list(topologyGrid)
allAntinodes = []
for antenna in allAntennas:
    antinodes = get_antinodes(antenna)
    for an in antinodes:
        if an not in allAntinodes:
            allAntinodes.append(an)
print(len(allAntinodes))
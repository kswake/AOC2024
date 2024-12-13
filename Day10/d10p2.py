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
        if not (int(x)+int(coordOffset[0]) < 0 or int(x)+int(coordOffset[0]) > int(map_size) or 
                int(y)+int(coordOffset[1]) < 0 or int(y)+int(coordOffset[1]) > int(map_size)):
            if int(trailmap[int(x)+int(coordOffset[0])][int(y)+int(coordOffset[1])]) == int(searchInt)+1:
                validNextSteps.append([int(x)+int(coordOffset[0]),int(y)+int(coordOffset[1]),searchInt+1])
    return validNextSteps

def count_distinct_trails(x, y, current_height):
    if current_height == 9:
        return 1
    trails = 0
    next_steps = get_next_steps(x, y, current_height)
    for step in next_steps:
        trails += count_distinct_trails(step[0], step[1], current_height + 1)
    return trails

def get_trail_rating(th_x, th_y):
    return count_distinct_trails(th_x, th_y, 0)

total_rating = 0
for trailhead in get_trailhead_coords(trailmap):
    total_rating += get_trail_rating(int(trailhead[0]), int(trailhead[1]))

print(total_rating)
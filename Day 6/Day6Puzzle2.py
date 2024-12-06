import os
from copy import deepcopy

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "puzzleInput6test.txt")

with open(file_path, "r") as mapInput:
    mapMaster = mapInput.read().splitlines()

directions = ["^", ">", "v", "<"]
MAX_STEPS = 100000

def get_pos(currMap):
    for r, line in enumerate(currMap):
        for c, ch in enumerate(line):
            if ch in directions:
                return [r, c]
    return None

def get_direction(currMap, pos):
    r, c = pos
    return currMap[r][c] if currMap[r][c] in directions else None

def turn_right(currDirection):
    return directions[(directions.index(currDirection) + 1) % 4]

def get_next_cell(pos, direction, currMap):
    row, col = pos
    if direction == "^":
        row -= 1
    elif direction == "v":
        row += 1
    elif direction == "<":
        col -= 1
    elif direction == ">":
        col += 1

    # Check boundaries:
    if row < 0 or row >= len(currMap) or col < 0 or col >= len(currMap[0]):
        # Out of bounds
        return [-1, -1]
    return [row, col]

def move_pointer(oldPos, newPos, direction, currMap):
    # Remove old direction from current position
    oldLine = currMap[oldPos[0]]
    oldDir = currMap[oldPos[0]][oldPos[1]]
    oldLine = oldLine[:oldPos[1]] + "." + oldLine[oldPos[1]+1:]
    currMap[oldPos[0]] = oldLine

    # Place the guard at the new position with the given direction
    newLine = list(currMap[newPos[0]])
    newLine[newPos[1]] = direction
    currMap[newPos[0]] = "".join(newLine)

    return currMap

def simulate_with_obstacle(currMap):
    """
    Simulate the guard's movement on currMap.
    Return True if the guard gets stuck in a loop, False if the guard leaves the map or if max steps are exceeded.
    """
    visited_states = set()
    # State is (row, col, direction)
    step_count = 0

    while step_count < MAX_STEPS:
        step_count += 1
        currPos = get_pos(currMap)
        if currPos is None:
            # Guard somehow not found - should not happen unless map corrupted
            return False

        direction = get_direction(currMap, currPos)
        if direction is None:
            # No direction found - invalid state
            return False

        state = (currPos[0], currPos[1], direction)
        if state in visited_states:
            # We've been in exactly this position and direction before - loop detected
            return True
        visited_states.add(state)

        nextPos = get_next_cell(currPos, direction, currMap)
        if nextPos == [-1, -1]:
            # Out of bounds - guard leaves the map
            return False

        # Check what is in the next cell
        nextCell = currMap[nextPos[0]][nextPos[1]]

        if nextCell == "#":
            # Turn right in place (no move)
            newDirection = turn_right(direction)
            line = list(currMap[currPos[0]])
            line[currPos[1]] = newDirection
            currMap[currPos[0]] = "".join(line)
            # Continue the loop after turning
        else:
            # Move forward into the next cell
            currMap = move_pointer(currPos, nextPos, direction, currMap)

    # If we reach here, we exceeded MAX_STEPS without finding a loop or exiting.
    # Assume no loop for practical purposes.
    return False

# Find the guard's start position so we never place an obstacle there
guard_start = get_pos(mapMaster)

loop_positions = []

for r in range(len(mapMaster)):
    for c in range(len(mapMaster[0])):
        # Conditions to place an obstacle:
        # 1. Must be originally '.' (free space)
        # 2. Can't be guard start
        # 3. Can't be '#' already
        if (r, c) != tuple(guard_start) and mapMaster[r][c] == ".":
            # Attempt placing an obstacle here
            testMap = [list(row) for row in mapMaster]
            testMap[r][c] = "#"  # Place temporary obstacle
            testMap = ["".join(row) for row in testMap]

            # Make a copy so we don't affect original map
            simMap = deepcopy(testMap)

            # Run simulation
            if simulate_with_obstacle(simMap):
                # We found a loop caused by placing an obstacle here
                loop_positions.append((r, c))

# Print results
print("Number of loop-causing positions:", len(loop_positions))
for pos in loop_positions:
    print("Row:", pos[0], "Col:", pos[1])

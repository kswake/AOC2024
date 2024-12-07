import os
import copy

# Define the possible directions and their corresponding movement deltas
DIRECTIONS = ["^", ">", "v", "<"]
DIR_TO_DELTA = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

def find_guard(map_state):
    """
    Locate the guard's starting position and direction on the map.
    Returns a tuple (row, col, direction) or None if not found.
    """
    for r in range(len(map_state)):
        for c in range(len(map_state[r])):
            if map_state[r][c] in DIRECTIONS:
                return (r, c, map_state[r][c])
    return None

def rotate_right(current_dir):
    """
    Rotate the current direction 90 degrees to the right.
    """
    index = DIRECTIONS.index(current_dir)
    return DIRECTIONS[(index + 1) % 4]

def simulate_guard(map_copy, guard_start_pos, guard_start_dir):
    """
    Simulate the guard's movement on the provided map_copy.
    Returns True if a loop is detected, False otherwise.
    """
    seen_states = set()
    guard_r, guard_c = guard_start_pos
    guard_dir = guard_start_dir

    while True:
        state = (guard_r, guard_c, guard_dir)
        if state in seen_states:
            # Loop detected
            return True
        seen_states.add(state)

        # Determine the next position based on current direction
        delta = DIR_TO_DELTA[guard_dir]
        next_r = guard_r + delta[0]
        next_c = guard_c + delta[1]

        # Check if the next position is out of bounds
        if not (0 <= next_r < len(map_copy) and 0 <= next_c < len(map_copy[0])):
            # Guard has left the map; no loop
            return False

        next_cell = map_copy[next_r][next_c]

        if next_cell in [".", "X"]:
            # Move forward
            map_copy[guard_r][guard_c] = "X"  # Mark current position as visited
            guard_r, guard_c = next_r, next_c
            map_copy[guard_r][guard_c] = guard_dir  # Update new position with current direction
        elif next_cell == "#":
            # Encountered an obstruction; turn right
            guard_dir = rotate_right(guard_dir)
            map_copy[guard_r][guard_c] = guard_dir  # Update direction on the map
        else:
            # Any other cell is treated as an obstruction; turn right
            guard_dir = rotate_right(guard_dir)
            map_copy[guard_r][guard_c] = guard_dir  # Update direction on the map

def main():
    # Read the map from the input file
    input_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "puzzleInput6.txt")
    with open(input_path, "r") as input_file:
        map_state = [list(line) for line in input_file.read().splitlines()]

    # Find the guard's starting position and direction
    guard_info = find_guard(map_state)
    if guard_info is None:
        print("Guard not found in the map.")
        return
    guard_start_r, guard_start_c, guard_start_dir = guard_info

    # Identify all possible obstruction positions (exclude starting position and existing obstructions)
    possible_obstructions = []
    for r in range(len(map_state)):
        for c in range(len(map_state[r])):
            if map_state[r][c] == '.' and not (r == guard_start_r and c == guard_start_c):
                possible_obstructions.append((r, c))

    loop_count = 0  # Initialize counter for valid obstruction positions

    # Iterate through each possible obstruction position
    for idx, (obs_r, obs_c) in enumerate(possible_obstructions, 1):
        # Create a deep copy of the map for simulation
        map_copy = copy.deepcopy(map_state)
        # Place the obstruction
        map_copy[obs_r][obs_c] = '#'
        # Simulate the guard's movement
        loop_detected = simulate_guard(map_copy, (guard_start_r, guard_start_c), guard_start_dir)
        if loop_detected:
            loop_count += 1
        # Optional: Progress tracking for large inputs
        if idx % 1000 == 0:
            print(f"Processed {idx} obstruction positions...")

    # Output the final count of valid obstruction positions
    print(f"Number of obstruction positions that cause a loop: {loop_count}")

if __name__ == "__main__":
    main()

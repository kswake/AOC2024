import os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day4input.txt")

with open(file_path, "r") as ws_text:
    ws_lines_master = [line.strip() for line in ws_text.readlines()]

def count_word_occurrences(grid, word):
    num_rows = len(grid)
    num_cols = len(grid[0])
    word_length = len(word)
    count = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    for row in range(num_rows):
        for col in range(num_cols):
            for dir in directions:
                match = True
                for k in range(word_length):
                    new_row = row + dir[0] * k
                    new_col = col + dir[1] * k
                    if (0 <= new_row < num_rows) and (0 <= new_col < num_cols):
                        if grid[new_row][new_col] != word[k]:
                            match = False
                            break
                    else:
                        match = False
                        break
                if match:
                    count += 1
    return count

print(count_word_occurrences(ws_lines_master,"XMAS"))
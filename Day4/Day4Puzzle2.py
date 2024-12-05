import os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day4input.txt")

with open(file_path, "r") as ws_text:
    ws_lines_master = [line.strip() for line in ws_text.readlines()]

def count_xmas_patterns(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])
    count = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 'A':
                diag1_valid = False
                diag2_valid = False
                row1, col1 = row - 1, col - 1
                row2, col2 = row + 1, col + 1
                if (0 <= row1 < num_rows and 0 <= col1 < num_cols and
                    0 <= row2 < num_rows and 0 <= col2 < num_cols):
                    c1 = grid[row1][col1]
                    c2 = grid[row2][col2]
                    if ( (c1 == 'M' and c2 == 'S') or (c1 == 'S' and c2 == 'M') ):
                        diag1_valid = True
                row3, col3 = row - 1, col + 1
                row4, col4 = row + 1, col - 1
                if (0 <= row3 < num_rows and 0 <= col3 < num_cols and
                    0 <= row4 < num_rows and 0 <= col4 < num_cols):
                    c3 = grid[row3][col3]
                    c4 = grid[row4][col4]
                    if ( (c3 == 'M' and c4 == 'S') or (c3 == 'S' and c4 == 'M') ):
                        diag2_valid = True
                if diag1_valid and diag2_valid:
                    count += 1
    return count

print(count_xmas_patterns(ws_lines_master))
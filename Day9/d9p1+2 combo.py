import os

def read_disk_map(filename):
    with open (os.path.join(os.path.dirname(os.path.abspath(__file__)),"d9input.txt"),'r') as f:
        return f.read().strip()

def parse_disk_map(s):
    segments = []
    is_file = True
    for ch in s:
        length = int(ch)
        if length > 0:
            segments.append((length, is_file))
        else:
            segments.append((0, is_file))
        is_file = not is_file
    return segments

def expand_segments(segments):
    blocks = []
    file_id = 0
    for length, is_file in segments:
        if is_file:
            for _ in range(length):
                blocks.append(file_id)
            file_id += 1
        else:
            for _ in range(length):
                blocks.append(None)
    return blocks

def compact_by_moving_individual_blocks(blocks):
    file_blocks = [b for b in blocks if b is not None]
    free_count = len(blocks) - len(file_blocks)
    return file_blocks + [None]*free_count

def compute_checksum(blocks):
    total = 0
    for i, b in enumerate(blocks):
        if b is not None:
            total += i * b
    return total

def compact_by_moving_whole_files(segments):
    original_blocks = expand_segments(segments)
    if not original_blocks:
        return original_blocks
    
    max_file_id = max(b for b in original_blocks if b is not None)
    blocks = original_blocks[:]

    def find_file_positions(blocks, fid):
        start = None
        end = None
        for i,b in enumerate(blocks):
            if b == fid:
                if start is None:
                    start = i
                end = i
        return start, end

    def find_free_segment(blocks, length, max_index):
        count = 0
        start = 0
        best_start = None
        for i in range(max_index):
            if blocks[i] is None:
                if count == 0:
                    start = i
                count += 1
                if count >= length:
                    best_start = start
                    break
            else:
                count = 0
        return best_start

    for fid in range(max_file_id, -1, -1):
        start, end = find_file_positions(blocks, fid)
        if start is None:
            continue
        file_len = end - start + 1
        free_start = find_free_segment(blocks, file_len, start)
        if free_start is not None:
            file_blocks = blocks[start:end+1]
            del blocks[start:end+1]
            blocks[start:start] = [None]*file_len

            for i in range(file_len):
                blocks[free_start+i] = file_blocks[i]

    return blocks

def main():
    s = read_disk_map("d9input.txt")
    segments = parse_disk_map(s)

    # p1
    blocks_part1 = expand_segments(segments)
    final_blocks_part1 = compact_by_moving_individual_blocks(blocks_part1)
    checksum_part1 = compute_checksum(final_blocks_part1)
    print("Part One Checksum:", checksum_part1)

    # p2
    final_blocks_part2 = compact_by_moving_whole_files(segments)
    checksum_part2 = compute_checksum(final_blocks_part2)
    print("Part Two Checksum:", checksum_part2)

if __name__ == "__main__":
    main()

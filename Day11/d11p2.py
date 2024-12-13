from collections import Counter

memo = {}

def split_even_digits(stone_str):
    length = len(stone_str)
    half = length // 2
    left_part = stone_str[:half]
    right_part = stone_str[half:]
    left_num = str(int(left_part))
    right_num = str(int(right_part))
    return left_num, right_num

def transform_once(stone_str):
    if stone_str == "0":
        return ["1"]
    else:
        length = len(stone_str)
        if length % 2 == 0:
            left_num, right_num = split_even_digits(stone_str)
            return [left_num, right_num]
        else:
            val = int(stone_str) * 2024
            return [str(val)]

def evolve(stone, steps):
    if steps == 0:
        return Counter([stone])
    key = (stone, steps)
    if key in memo:
        return memo[key]
    new_stones = transform_once(stone)
    result_counter = Counter()
    for st in new_stones:
        result_counter.update(evolve(st, steps - 1))

    memo[key] = result_counter
    return result_counter

initial_stones = "3 386358 86195 85 1267 3752457 0 741".split()
steps = 75

final_distribution = Counter()
for st in initial_stones:
    final_distribution.update(evolve(st, steps))

print(sum(final_distribution.values()))

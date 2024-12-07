import os
from itertools import product

with open (os.path.join(os.path.dirname(os.path.abspath(__file__)),"d7input.txt"), "r") as input:
    calcsMaster = []
    for line in input:
        result, operands = line.split(":")
        result = int(result.strip())
        values_list = list(map(int, operands.split()))
        calcsMaster.append([result, values_list])

def get_operator_matrix(numOps):
    return product(['+', '*'], repeat=numOps)

def evaluate_expr(nums, ops):
    currResult = nums[0]
    for op, num in zip(ops, nums[1:]):
        if op == "+":
            currResult = currResult + num
        else:
            currResult = currResult * num
    return currResult


runningTotal = 0
for target, nums in calcsMaster:

    numOps = len(nums) - 1
    solvable = False

    for ops in get_operator_matrix(numOps):
        currResult = evaluate_expr(nums, ops)
        if currResult == target:
            solvable = True
            break

    if solvable:
        runningTotal += target

print(runningTotal)

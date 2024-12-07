import os
from itertools import product

with open (os.path.join(os.path.dirname(os.path.abspath(__file__)),"d7input.txt"), "r") as input:
    calcsMaster = []
    for line in input:
        result, operands = line.split(":")
        result = int(result.strip())
        values_list = list(map(int, operands.split()))
        calcsMaster.append([result, values_list])

def get_num_perms(operands): #not using right not, don't know if I need this
    return (2**(len(operands)-1))

def get_operator_matrix(numOps):
    return list(product(['+','*'], repeat=numOps))

##Logic here is wrong somehow
def evaluate_expr(target,nums,ops): #evaluate a given numbers/operators combo. immediately return 0 if a given branch exceeds target
    
    currResult = nums[0]

    for op, num in zip(ops,nums[1:]):
        if op == "+":
            currResult = currResult + num
        else:
            currResult = currResult * num

        if currResult>target:
            return 0
        
    return currResult


runningTotal = 0
for item in calcsMaster:
    itemResult = evaluate_expr(item[0],item[1],get_operator_matrix(len(item[1])))
    if itemResult == 0:
        runningTotal+=0
    else:
        runningTotal = runningTotal + itemResult 
print(runningTotal)
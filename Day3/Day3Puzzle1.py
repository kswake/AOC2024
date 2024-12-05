import os
import re

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day3puzzleinput.txt")

def compMul(currMul):
    op_split = str(currMul).split(r',')
    op1 = op_split[0].replace("mul(","")
    op2 = op_split[1].replace(")","")
    return(int(op1) * int(op2))

with open(file_path,"r") as file_load:
    mem = file_load.read()

mul_re = re.compile(r'mul\(\d+,\d+\)')
validMuls = re.findall(mul_re,mem)

mulSum = 0
for mul in validMuls:
    mulSum = mulSum + compMul(mul)

print(mulSum)
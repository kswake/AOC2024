import os
import re

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, "day3puzzleinput.txt")

def compMul(currMul):
    op_split = str(currMul).split(r',')
    op1 = op_split[0].replace("mul(","")
    op2 = op_split[1].replace(")","")
    return(int(op1) * int(op2))

with open(file_path,"r") as file_load:
    mem = file_load.read()

condMul_re = re.compile(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)')
validCondMuls = re.findall(condMul_re,mem)

mulSum = 0
mul_enabled = True #by default until "don't()"

for item in validCondMuls:
    isMul = True

    if item == "don't()":
        mul_enabled = False
        isMul = False
    elif item == "do()":
        mul_enabled = True
        isMul = False
        
    if mul_enabled == True and isMul == True:
        mulSum += compMul(item) 

print(mulSum)


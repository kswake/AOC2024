import os

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day4input.txt")

with open(file_path, "r") as ws_text:
    ws_lines_master = ws_text.readlines()

def find_h(ws_line, findStr_h):
    occurrence = 0
    for i in range(len(ws_line)-3):
        checkStr = str(ws_line[i]) + str(ws_line[i+1]) + str(ws_line[i+2]) + str(ws_line[i+3])
        if checkStr == findStr_h:
            occurrence+=1
    return occurrence

def find_v(lines_total, findStr_v):
    occurrence = 0
    for i in range(len(lines_total)-3):
        line1 = lines_total[i]
        line2 = lines_total[i+1]
        line3 = lines_total[i+2]
        line4 = lines_total[i+3]

        for j in range(len(line1)-1):
            checkStr_v = str(line1[j]) + str(line2[j]) + str(line3[j]) + str(line4[j])
            if checkStr_v == findStr_v:
                print(str(i) + " " + str(j) + " " + checkStr_v + "FOUND!")
            else:
                print(str(i) + " " + str(j) + " " + checkStr_v)    
    return occurrence

xmasSum = 0

for line in ws_lines_master:
    xmasSum += find_h(line,"XMAS")
    xmasSum += find_h(line,"SAMX")
    xmasSum += find_v(ws_lines_master,"XMAS")
    xmasSum += find_v(ws_lines_master,"SAMX")

print(xmasSum)


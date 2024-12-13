stones = str("3 386358 86195 85 1267 3752457 0 741").split()

def blink(stones):
    insertables = []
    for position in range(len(stones)):

        if int(stones[position]) == 0:

            stones[position] = 1

        elif len(str(stones[position]))%2==0:

            splitStones = [d for d in str(stones[position])]
            stone1_digits = splitStones[int(len(splitStones)/2):]
            stone1 = ""
            for i in range(len(stone1_digits)):
                stone1 += str(stone1_digits[i])
            stones[position]=int(stone1)

            stone2_digits = splitStones[:int(len(splitStones)/2)]
            stone2 = ""
            for j in range(len(stone2_digits)):
                stone2 += str(stone2_digits[j])
            stone2 = int(stone2)
            insertables.append([position, int(stone2)])

        else:

            stones[position] = int(stones[position]) * 2024
  
    offset = 0
    if insertables is not None: 
        for insertable in insertables:
            stones.insert(insertable[0]+offset,insertable[1])
            offset+=1

for i in range(0,75):
    blink(stones)

print(len(stones))

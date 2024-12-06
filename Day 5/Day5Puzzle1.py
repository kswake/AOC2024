import os
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "day5input.txt")

with open(file_path, "r") as puzzleInput:
    inputMaster = puzzleInput.readlines()
pageOrders = []
updateSet = []
for item in inputMaster:
    if "|" in str(item):
        pageOrders.append(str(item).strip().split("|"))
    elif "," in str(item):
        updateSet.append(str(item).strip().split(","))

def get_pageorder_for_update(update):
    applicableOrders = []
    for page in update:
        for order in pageOrders:
            if page == order[0]:
                if order[1] in update:
                    applicableOrders.append(order)
    return applicableOrders

def validate_page_order(update, appOrderSet):
    for page in update:
        for order in appOrderSet:
            if page == order[0]:
                if order[1] in update:
                    if update.index(order[1]) < update.index(order[0]):
                        return False
    return True

midNumSum = 0
for update in updateSet:
    currOrderSet = get_pageorder_for_update(update)
    if validate_page_order(update, currOrderSet) == True:
        midNumSum += int(update[(int(((len(update)-1)/2)))])
print(midNumSum)
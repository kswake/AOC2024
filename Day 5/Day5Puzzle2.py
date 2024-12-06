import os
from collections import deque

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

def topological_sort(update, appOrderSet):
    pages = update[:]
    page_set = set(pages)
    adj = {p: [] for p in pages}
    indeg = {p: 0 for p in pages}
    for x, y in appOrderSet:
        adj[x].append(y)
        indeg[y] += 1
    queue = deque([p for p in pages if indeg[p] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for nxt in adj[node]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                queue.append(nxt)
    if len(result) != len(pages):
        pass
    return result

def get_middle_page(update):
    n = len(update)
    return int(update[n // 2])

midNumSum = 0
reorderedUpdates = []

for update in updateSet:
    currOrderSet = get_pageorder_for_update(update)

    if not validate_page_order(update, currOrderSet):
        corrected_order = topological_sort(update, currOrderSet)
        reorderedUpdates.append(corrected_order)

for eachUpdate in reorderedUpdates:
    midNumSum += get_middle_page(eachUpdate)

print(midNumSum)
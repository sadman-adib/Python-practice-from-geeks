# Difference between two lists

list1 = set([10, 15, 20, 25, 30, 35, 40])
list2 = set([25, 40, 35])

diff = list(list1 - list2)

print(diff)
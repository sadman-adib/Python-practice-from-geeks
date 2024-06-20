# Python program to find common elements in three lists using sets

list1 = set([1,1,1,1,1,1,2,2,2,2,2,2,3,4,5])
list2 = set([2,2,2,2,6,7])
list3 = set([2,2,2,2,6,7,8,9])

common_elements = ((list1.intersection(list2)).intersection(list3))

print( "common elements from 3 lists :",  common_elements)
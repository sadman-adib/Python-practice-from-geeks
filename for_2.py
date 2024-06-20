keys = ['apple','ball','cat','dog','egg']

values = [1,2,3,4,5]  
  
myDict = { k:v for (k,v) in zip(keys, values)}  # list to dict

print (myDict)
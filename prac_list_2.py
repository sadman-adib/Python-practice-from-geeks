odd_square = [] # odd number from 0-12 and square of them

for i in range(0,12): 
    if(i % 2 == 1): # 1,3,5,7,9,11
        odd_square.append(i**2)

print(odd_square)
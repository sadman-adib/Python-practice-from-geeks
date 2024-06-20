matrix = [] 
  
for i in range(3): 
  
    # Append an empty sublist inside the list 
    matrix.append([str(i)]) # 1st element of each sub list 
  
    for j in range(4): 
        matrix[i].append(j) # all elements of each sub list after 1st element
  
print(matrix) 
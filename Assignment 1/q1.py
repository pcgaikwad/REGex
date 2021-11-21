rows = int(input("Enter the number of rows: "))  
  
# the outer loop is executing in reversed order  
for i in range(rows , 0, -1):    
    for j in range(0, i):  
        print(rows, end=' ')  
    print(" ")  
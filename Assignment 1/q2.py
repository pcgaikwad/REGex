#Task 1
#Name: Prathmesh Chhaganrao Gaikwad
rows = int(input("Enter the number of rows: ")) 

# the outer loop is executing in reversed order  
for i in range(rows + 1, 1, -1):
    for j in range(0, i ):
        print(j, end=' ')
    print(" ")
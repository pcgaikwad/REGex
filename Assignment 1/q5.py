#Task 1
#Name: Prathmesh Chhaganrao Gaikwad
i = 1
j = 2
now = j
for row in range(2, 6):
    for col in range(i, j):
        now -= 1
        print(now, end=' ')
    print("")
    i = j
    j += row
    now = j

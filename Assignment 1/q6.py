def triangle(size):
    for i in range(0, size):
        for j in range(0, i + 1):
            print(decider(i, j), end=" ")
        print()


def decider(n, k):
    num = 1
    if k > n - k:
        k = n - k
    for i in range(0, k):
        num = num * (n - i)
        num = num // (i + 1)
    return num

rows = 7
triangle(rows)

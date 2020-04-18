def vestigium(A, n, num):
    trace = 0
    r = 0
    c = 0
    for i in range(n):
        trace += A[i][i]
        row = A[i]
        if len(set(row)) < len(row):
            r += 1
        col = [row[i] for row in A]
        if len(set(col)) < len(col):
            c += 1

    output = "Case #{}: {} {} {}".format(num+1, trace, r, c)
    return(output)

t = int(input()) # number of test cases
for num in range(t):
    n = int(input()) # size of matrix
    A = []
    for j in range(n):
        row = input().split()
        row = [int(x) for x in row]
        A = A + [row]
    print(vestigium(A, n, num))

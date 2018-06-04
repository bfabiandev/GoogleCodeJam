T = int(input())
for i in range(1, T + 1):
    N = int(input())
    weigths = [int(j) for j in input().split()]
    weigths.reverse()
    table = [[-1 for _ in range(N+1)] for _ in range(N+1)]
    for j in range(N+1):
        table[0][j] = 1e12
    for col in range(1, N+1):
        for row in range(1, N+1):
            if row > col:
                continue
            
            table[row][col] = max(table[row][col-1], min(table[row-1][col-1] - weigths[col-1], weigths[col-1]*6))

    largest_row = 0
    for row in range(1, N+1):
        if table[row][-1] >= 0:
            largest_row = row

    print("Case #{}: {}".format(i, largest_row))

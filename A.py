T = int(input())
for i in range(1, T + 1):
    [D, N] = [int(i) for i in input().split()]
    horses = []
    for j in range(N):
        [K, S] = [float(i) for i in input().split()]
        horses.append((D - K)/S)
    m = max(horses)
    print("Case #{}: {:.6f}".format(i, D / m))
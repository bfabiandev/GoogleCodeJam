T = int(input())
for i in range(1, T + 1):
    [D, P] = [i for i in input().split()]
    D = int(D)
    minimum = P.count('S')
    if minimum > D:
        print("Case #{}: {}".format(i, 'IMPOSSIBLE'))
        continue

    S = 0
    current = 1
    shots = list()
    for ch in P:
        if ch == 'C':
            current *= 2
        else:
            shots.append(current)

    steps = 0
    while sum(shots) > D:
        steps += 1
        m = max(shots)
        shots.remove(m)
        shots.append(m // 2)
    print("Case #{}: {}".format(i, steps))
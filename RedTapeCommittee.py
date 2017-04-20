import numpy as np


def chance_of_tie(ps):
    l = np.zeros(shape=(len(ps) + 1, 1))
    l[0] = 1.0 - ps[0]
    l[1] = ps[0]

    for i in ps[1:]:
        temp = np.roll(l, 1)
        temp[0] = 0
        l1 = (1.0 - i) * l + i * temp
        l = l1.copy()

    return l[int(len(ps) / 2)]


T = int(input())
for i in range(1, T + 1):
    [N, K] = [int(i) for i in input().split()]
    P = [float(i) for i in input().split()]

    P.sort()

    bestP = P[0:K]
    best = chance_of_tie(bestP)

    for M in range(K):
        temp = P[0:M] + P[-K + M:]
        result = chance_of_tie(temp)
        if result > best:
            best = result
            bestP = temp

    print("Case #{}: {:.8f}".format(i, best[0]))

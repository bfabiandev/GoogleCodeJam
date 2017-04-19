import math

import itertools


def binom(n, k):
    ret = 0
    if n == k:
        ret = 1
    elif k == 1:
        ret = n
    else:
        a = math.factorial(n)
        b = math.factorial(k)
        c = math.factorial(n - k)
        ret = a // (b * c)
    return ret


numbers = []
d = dict()
for n in range(13):
    P = 0
    R = 0
    S = 0
    for i in range(n+1):
        if i % 3 == 0:
            P += binom(n, i)
        elif i % 3 == 1:
            R += binom(n, i)
        else:
            S += binom(n, i)
    numbers.append([n, P, R, S])
    d["{} {} {} {}".format(n, P, R, S)] = 'P'
    numbers.append([n, R, S, P])
    d["{} {} {} {}".format(n, R, S, P)] = 'S'
    numbers.append([n, S, P, R])
    d["{} {} {} {}".format(n, S, P, R)] = 'R'

T = int(input())


def gen(possibilities, n):
    new_poss = []
    for p in possibilities:
        temp = []
        for i in p:
            temp2 = []
            if i == 'P':
                temp2.append('PR')
                temp2.append('RP')
            elif i == 'R':
                temp2.append('RS')
                temp2.append('SR')
            else:
                temp2.append('PS')
                temp2.append('SP')
            if len(temp) == 0:
                temp.extend(temp2)
            else:
                temp = [a+b for (a,b) in list(itertools.product(temp, temp2))]
        new_poss.extend(temp)
    return new_poss



for i in range(1, T + 1):
    [N, R, P, S] = [int(i) for i in input().split()]
    if [N, R, P, S] not in numbers:
        print("Case #{}: {}".format(i, "IMPOSSIBLE"))
    else:
        possibilities = d["{} {} {} {}".format(N, P, R, S)]
        for j in range(N):
            possibilities = gen(possibilities, j)
        possibilities.sort()
        print("Case #{}: {}".format(i, possibilities.pop(0)))

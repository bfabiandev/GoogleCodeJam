import itertools

def cross_path(pair1, pair2):
    x = set(range(pair1[0], pair1[1]))
    y = set(range(pair2[0], pair2[1]))
    intersect = x.intersection(y)
    if len(intersect) == len(y) or len(intersect) == len(x) or len(intersect) == 0:
        return False
    else:
        return True

T = int(input())
for i in range(1, T + 1):
    [R, C] = [int(i) for i in input().split()]
    pairs = [int(i) for i in input().split()]
    i1 = iter(pairs)
    pairs = list(zip(i1, i1))
    temps = []
    for pair in pairs:
        if pair[0] > pair[1]:
            temp = tuple(reversed(pair))
            temps.append(temp)
        else:
            temps.append(pair)
    pairs = temps
    pairs.sort()

    cp = False

    for u,v in itertools.combinations(pairs, 2):
        if cross_path(pair1=u, pair2=v):
            cp = True
            break
    if cp:
        print("Case #{}: {}".format(i, 'IMPOSSIBLE'))
    else:
        print("Case #{}:".format(i))

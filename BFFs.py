t = int(input())
for i in range(1, t + 1):
    N = int(input())
    line = [int(x) for x in input().split()]
    d = {i+1: line[i] for i in range(len(line))}

    circles = []
    max_circle = 0
    ls = []
    for j in range(1, N+1):
        temp = [j]
        for _ in range(N):
            temp.append(d[temp[-1]])

            if d[temp[-1]] == temp[0] and len(temp) > 2:
                circles.append((j, temp))
                max_circle = max(max_circle, len(temp))
                break
            elif d[temp[-1]] == temp[-2]:
                ls.append(temp)
                break

    ls = sorted(ls, key=lambda x: len(x))
    ld = {}
    for l in ls:
        if l[-1] not in ld:
            ld[l[-1]] = len(l)
        else:
            ld[l[-1]] = max(len(l), ld[l[-1]])

    max_ls = 1
    l2circle = {}

    # TODO concatenate all the independent components with a circle-size of 2
    if len(ld) != 0:
        for key in ld.keys():
            key_pair = d[key]
            l2circle[(min(key, key_pair), max(key, key_pair))] = ld[key] + ld[key_pair] - 2

    max_ls = sum(x for x in l2circle.values())

    print("Case #{}: {}".format(i, max(max_ls, max_circle, 1)))

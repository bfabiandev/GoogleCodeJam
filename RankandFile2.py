t = int(input())
for i in range(1, t + 1):
    N = int(input())
    lines = []
    for _ in range(2 * N - 1):
        line = [int(x) for x in input().split()]
        lines.extend(line)
    lines.sort()
    sol = []

    counter = 0
    last = lines[0]
    for j in lines:
        if j == last:
            counter += 1
        else:
            if counter % 2 != 0:
                sol.append(last)
            last = j
            counter = 1
    if counter % 2 != 0:
        sol.append(last)

    print("Case #{}: {}".format(i, " ".join(str(x) for x in sol)))

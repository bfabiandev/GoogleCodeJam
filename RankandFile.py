t = int(input())
for i in range(1, t + 1):
    N = int(input())
    lines = []
    for _ in range(2 * N - 1):
        line = [int(x) for x in input().split()]
        lines.append(line)
    lines.sort()

    sol = []
    for _ in range(N):
        first = lines.pop(0)
        if len(lines) == 0:
            sol.append(first[0])
            break
        elif lines[0][0] == first[0]:
            second = lines.pop(0)
            rest = second[1:] + first[1:]
            rest.sort()
            for line in lines:
                rest.remove(line[0])
            sol.append(rest[0])
            linesT = list(map(list, zip(*lines)))
            linesT.pop(0)
            lines = list(map(list, zip(*linesT)))
            lines.sort()
        else:
            sol.append(first[0])
            for j in first[1:]:
                for line in lines:
                    if line[0] == j:
                        lines.remove(line)
                        break

            for line in lines:
                sol.append(line[0])
            break

    print("Case #{}: {}".format(i, " ".join(str(x) for x in sol)))

def finish(a, b):
    larger = 0
    a = a.copy()
    b = b.copy()
    for j in range(len(a)):
        if larger == 0:
            if a[j] == b[j]:
                continue
            else:
                if a[j] == '?':
                    a[j] = b[j]
                elif b[j] == '?':
                    b[j] = a[j]

                if a[j] > b[j]:
                    larger = 1
                else:
                    larger = -1
        elif larger == 1:
            if a[j] == b[j]:
                if a[j] == '?':
                    a[j] = '0'
                    b[j] = '9'
                else:
                    pass
            else:
                if a[j] == '?':
                    a[j] = '0'
                elif b[j] == '?':
                    b[j] = '9'
                else:
                    pass
        else:
            if a[j] == b[j]:
                if a[j] == '?':
                    a[j] = '9'
                    b[j] = '0'
                else:
                    pass
            else:
                if a[j] == '?':
                    a[j] = '9'
                elif b[j] == '?':
                    b[j] = '0'
                else:
                    pass
    return a, b

def decide(tempC,tempJ, bestC, bestJ, bestDif):
    tempDif = abs(int("".join(x for x in tempC)) - int("".join(x for x in tempJ)))
    if tempDif < bestDif:
        bestC = tempC
        bestJ = tempJ
        bestDif = tempDif
    elif tempDif == bestDif:
        if tempC < bestC:
            bestC = tempC
            bestJ = tempJ
            bestDif = tempDif
        elif tempC == bestC:
            if tempJ < bestJ:
                bestC = tempC
                bestJ = tempJ
                bestDif = tempDif
    return bestC, bestJ, bestDif

T = int(input())
for i in range(1, T+1):
    C, J = [list(s) for s in input().split()]
    larger = 0

    bestC = []
    bestJ = []
    bestDif = 2**80

    for j in range(len(C)):
        if C[j] == J[j] and C[j] != '?':
            continue

        if C[j] != J[j] and C[j] != '?' and J[j] != '?':
            tempC, tempJ = finish(C, J)
            bestC, bestJ, bestDif = decide(tempC, tempJ, bestC, bestJ, bestDif)
            C = bestC
            J = bestJ
            break
        if C[j] != J[j] and (C[j] == '?' or J[j] == '?'):
            if C[j] == '?':
                if int(J[j]) != 0:
                    C[j] = str(int(J[j]) - 1)
                    tempC, tempJ = finish(C, J)
                    bestC, bestJ, bestDif = decide(tempC, tempJ, bestC, bestJ, bestDif)

                if int(J[j]) != 9:
                    C[j] = str(int(J[j]) + 1)
                    tempC, tempJ = finish(C, J)
                    bestC, bestJ, bestDif = decide(tempC, tempJ, bestC, bestJ, bestDif)

                C[j] = J[j]

            elif J[j] == '?':
                if int(C[j]) != 0:
                    J[j] = str(int(C[j]) - 1)
                    tempC, tempJ = finish(C, J)
                    bestC, bestJ, bestDif = decide(tempC, tempJ, bestC, bestJ, bestDif)

                if int(C[j]) != 9:
                    J[j] = str(int(C[j]) + 1)
                    tempC, tempJ = finish(C, J)
                    bestC, bestJ, bestDif = decide(tempC, tempJ, bestC, bestJ, bestDif)

                J[j] = C[j]

            continue
        if C[j] == '?' and J[j] == '?':
            C[j] = '0'
            J[j] = '1'
            tempC, tempJ = finish(C, J)
            bestC, bestJ, bestDif = decide(tempC, tempJ, bestC, bestJ, bestDif)

            C[j] = '1'
            J[j] = '0'
            tempC, tempJ = finish(C, J)
            bestC, bestJ, bestDif = decide(tempC, tempJ, bestC, bestJ, bestDif)

            C[j] = '0'
            J[j] = '0'

            continue

    bestC, bestJ, bestDif = decide(C, J, bestC, bestJ, bestDif)

    print("Case #{}: {} {}".format(i, "".join(str(x) for x in bestC), "".join(str(x) for x in bestJ)))

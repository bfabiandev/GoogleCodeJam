from enum import Enum


def biggestF(R, Y, B):
    if R >= Y and R >= B:
        return 'R'
    if Y >= R and Y >= B:
        return 'Y'
    if B >= R and B >= Y:
        return 'B'


def perfect(S):
    for i in range(len(S)-1):
        if S[i] == S[i + 1]:
            return i

    if S[-1] == S[0]:
        return len(S)-1
    return None


class Color(Enum):
    RED = 1
    YELLOW = 2
    BLUE = 3


T = int(input())
for i in range(1, T + 1):
    [N, R, O, Y, G, B, V] = [int(i) for i in input().split()]
    if (R <= G and R + G < N and R + G > 0) \
            or (B <= O and B + O < N and B + O > 0) \
            or (Y <= V and Y + V < N and Y + V > 0):
        print("Case #{}: {}".format(i, 'IMPOSSIBLE'))
        continue
    R1 = R - G
    Y1 = Y - V
    B1 = B - O
    d = {0: R1, 1: Y1, 2: B1}

    if B1 > Y1 + R1 or R1 > Y1 + B1 or Y1 > B1 + R1:
        print("Case #{}: {}".format(i, 'IMPOSSIBLE'))
        continue

    result = ""

    if R > G:
        Rrest = "R" + "GR" * G
    else:
        Rrest = "GR" * G
    if Y > V:
        Yrest = "Y" + "VY" * V
    else:
        Yrest = "VY" * V
    if B > O:
        Brest = "B" + "OB" * O
    else:
        Brest = "OB" * O

    SUM = d[0] + d[1] + d[2]
    for _ in range(SUM):
        biggest = biggestF(d[0], d[1], d[2])
        if len(result) > 0 and result[-1] == biggest:
            if biggest == 'R':
                if d[1] >= d[2]:
                    biggest = 'Y'
                else:
                    biggest = 'B'
            elif biggest == 'Y':
                if d[2] >= d[0]:
                    biggest = 'B'
                else:
                    biggest = 'R'
            else:
                if d[0] >= d[1]:
                    biggest = 'R'
                else:
                    biggest = 'Y'
        result += biggest
        if biggest == 'R':
            d[0] -= 1
        elif biggest == 'Y':
            d[1] -= 1
        else:
            d[2] -= 1

    if len(result) > 0:
        if result[0] == result[-1]:
            result = result[0:-2] + result[-1] + result[-2]
        counter = 0
        while perfect(result) is not None:
            idx = perfect(result)
            result = result[0:idx-1] + result[idx] + result[idx-1]
            counter += 1
            if counter > 1000:
                print('ELBASZTAD ' + result)
                break
        result = result.replace('R', Rrest, 1)
        result = result.replace('Y', Yrest, 1)
        result = result.replace('B', Brest, 1)
    else:
        result = Rrest + Yrest + Brest

    print("Case #{}: {}".format(i, result))

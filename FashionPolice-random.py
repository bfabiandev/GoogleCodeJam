import random

T = int(input())


def valid(outfit, solution):
    if outfit in solution:
        return False
    K1 = 0
    K2 = 0
    K3 = 0
    for sol in solution:
        if outfit[0] == sol[0] and outfit[1] == sol[1]:
            K1 += 1
        if outfit[0] == sol[0] and outfit[2] == sol[2]:
            K2 += 1
        if outfit[1] == sol[1] and outfit[2] == sol[2]:
            K3 += 1
        if K1 >= K or K2 >= K or K3 >= K:
            return False
    return True


for i in range(1, T + 1):
    [J, P, S, K] = [int(i) for i in input().split()]
    max_possible = J*P*min(K, S)
    print("Case #{}: {}".format(i, max_possible))
    outfits = []
    for ji in range(J):
        for pi in range(P):
            for si in range(S):
                outfits.append([ji+1, pi+1, si+1])

    solution = []
    while len(solution) < max_possible:
        solution = []
        random.shuffle(outfits)

        for outfit in outfits:
            if valid(outfit, solution):
                solution.append(outfit)

            if len(solution) == max_possible:
                break

    for combo in solution:
        print("{} {} {}".format(combo[0], combo[1], combo[2]))




T = int(input())
for i in range(1, T + 1):
    [J, P, S, K] = [int(i) for i in input().split()]

    print("Case #{}: {}".format(i, J*P*min(K, S)))
    for ji in range(J):
        for pi in range(P):
            for ki in range(min(K,S)):
                print("{} {} {}".format(ji+1, pi+1, (ji+pi+ki) % S + 1))

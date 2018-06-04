def solve(cashier, time):
    M, S, P = cashier
    N = max(0, min((time - P) // S, M))
    return N

def solve_all(cashiers, time, R):
    performances = [solve(cashier, time) for cashier in cashiers]
    performances.sort(reverse=True)
    summa = sum(performances[:R])
    return summa

T = int(input())
for i in range(1, T+1):
    [R, B, C] = [int(s) for s in input().split()]
    cashiers = []
    for c in range(C):
        [M, S, P] = [int(s) for s in input().split()]
        cashiers.append((M, S, P))
    

    high = 1
    while solve_all(cashiers, high, R) < B:
        high *= 2
    low = high // 2

    while high > low:
        mid = (low + high) // 2
        N = solve_all(cashiers, mid, R)
        if N < B:
            low = mid + 1
        else:
            high = mid

    print("Case #{}: {}".format(i, high))

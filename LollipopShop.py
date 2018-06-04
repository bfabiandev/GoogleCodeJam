import sys

def solve(D, prefs, not_used, seen):
    prefs = [j for j in prefs if j in not_used]
    argmin, mini = -1, 1000000
    for p in prefs:
        if seen[p] < mini:
            argmin = p
            mini = seen[p]
            if p == 0:
                break

    if argmin in not_used:
        not_used.remove(argmin)
    for p in prefs:
        seen[p] += 1

    print(argmin)
    sys.stdout.flush()

    return not_used, seen
    
T = int(input())
for _ in range(T):
    N = int(input())
    not_used = set([i for i in range(N)])
    seen = [0 for i in range(N)]
    for _ in range(N):
        inp = [int(i) for i in input().split()]
        D = inp.pop(0)
        not_used, seen = solve(D, inp, not_used, seen)
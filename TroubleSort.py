from itertools import zip_longest

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    V = [int(j) for j in input().split()]

    V_even = [j for j in V[::2]]
    V_odd = [j for j in V[1::2]]

    V_even.sort()
    V_odd.sort()

    V_sorted = [item for items in zip_longest(V_even, V_odd) for item in items
                if item is not None]

    if all(V_sorted[j] <= V_sorted[j + 1] for j in range(len(V_sorted) - 1)):
        print("Case #{}: {}".format(i, 'OK'))
        continue

    for idx in range(len(V_sorted) - 1):
        if V_sorted[idx] > V_sorted[idx + 1]:
            print("Case #{}: {}".format(i, idx))
            break


t = int(input())
for i in range(1, t + 1):
    s = input()
    sol = ""
    for c in s:
        if len(sol) == 0 or sol[0] <= c:
            sol = c + sol
        else:
            sol = sol + c

    print("Case #{}: {}".format(i, sol))

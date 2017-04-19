T = int(input())
for i in range(1, T + 1):
    [R, C] = [int(i) for i in input().split()]
    cake = []
    for j in range(R):
        cake.append(list(input()))

    new_cake = []
    for row in cake:
        if row != "?" * C:
            last_ch = None
            new_row = ""
            for k, ch in enumerate(row):
                if ch == "?":
                    if last_ch is None:
                        new_row += "?"
                    else:
                        new_row += last_ch
                else:
                    last_ch = ch
                    new_row += ch
            new_cake.append(list(new_row))

    cake = new_cake.copy()
    new_cake = []
    for row in list(reversed(cake)):
        if row != "?" * C:
            last_ch = None
            new_row = ""
            for ch in list(reversed(row)):
                if ch == "?":
                    if last_ch is None:
                        new_row += "?"
                    else:
                        new_row += last_ch
                else:
                    last_ch = ch
                    new_row += ch
            new_cake.append(list(reversed(new_row)))
    cake = list(reversed(new_cake))

    first_normal_row = False
    first_normal_row_idx = -1
    new_cake = []
    for j, row in enumerate(cake):
        if row == list("?" * C):
            if first_normal_row:
                new_cake.append(new_cake[j - 1])
            else:
                new_cake.append(row)
        else:
            new_cake.append(row)
            if not first_normal_row:
                first_normal_row = True
                first_normal_row_idx = j

    cake = new_cake
    cake[0:first_normal_row_idx] = [cake[first_normal_row_idx]]*first_normal_row_idx

    print("Case #{}:".format(i))
    for row in cake:
        print(''.join(row))

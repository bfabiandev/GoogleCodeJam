T = int(input())
for i in range(1, T + 1):
    [R, C, H, V] = [int(i) for i in input().split()]
    waffle = []
    for line in range(R):
        waffle.append(input())
    
    waffle_rows = []
    for row in waffle:
        waffle_rows.append(row.count('@'))

    waffle_cols = []
    for col in range(C):
        waffle_cols.append(sum([1 for line in waffle if line[col] == '@']))

    n_chips = sum(waffle_cols)
    if n_chips % ((H + 1) * (V + 1)) != 0:
        print("Case #{}: {}".format(i, 'IMPOSSIBLE'))
        continue
    
    if n_chips == 0:
        print("Case #{}: {}".format(i, 'POSSIBLE'))
        continue

    cum_sum_row = []
    cum_sum_col = []    
    for row in waffle_rows:
        if len(cum_sum_row) == 0:
            cum_sum_row.append(row)
        else:
            cum_sum_row.append(row + cum_sum_row[-1])

    for col in waffle_cols:
        if len(cum_sum_col) == 0:
            cum_sum_col.append(col)
        else:
            cum_sum_col.append(col + cum_sum_col[-1])

    row_intervals = []
    prev = 0
    error = False

    for border in range(n_chips // (H + 1), n_chips+1, n_chips // (H + 1)):
        try:
            idx = cum_sum_row.index(border)
            row_intervals.append((prev, idx))
            prev = idx + 1
        except ValueError:
            error = True
            break

    if error:
        print("Case #{}: {}".format(i, 'IMPOSSIBLE'))
        continue


    col_intervals = []
    prev = 0
    error = False
    for border in range(n_chips // (V + 1), n_chips+1, n_chips // (V + 1)):
        try:
            idx = cum_sum_col.index(border)
            col_intervals.append((prev, idx))
            prev = idx + 1
        except ValueError:
            error = True
            break

    if error:
        print("Case #{}: {}".format(i, 'IMPOSSIBLE'))
        continue

    impossible = False
    for col_int in col_intervals:
        for row_int in row_intervals:
            chips = 0
            row_start, row_finish = row_int
            col_start, col_finish = col_int
            for chunk in waffle[row_start:row_finish+1]:
                chips += sum([1 for cell in chunk[col_start:col_finish+1] if cell == '@'])

            if chips !=  n_chips // ((H + 1) * (V + 1)):
                impossible = True
                break
        if impossible:
            break
    
    if impossible:
        print("Case #{}: {}".format(i, 'IMPOSSIBLE'))
        continue

    print("Case #{}: {}".format(i, 'POSSIBLE'))

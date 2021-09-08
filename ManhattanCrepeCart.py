import numpy as np

T = int(input())
for i in range(1, T + 1):
    P, Q = [int(k) for k in input().strip().split(' ')]
    peeps = []
    for _ in range(P):
        peeps.append(input().strip().split(' '))

    grid = np.zeros((Q, Q), dtype=int)

    for peep in peeps:
        X, Y, D = peep
        X = int(X)
        Y = int(Y)
        if D == 'N':
            grid[:, Y + 1:] += np.ones((Q, Q - Y - 1), dtype=int)
        elif D == 'S':
            grid[:, :Y] += np.ones((Q, Y), dtype=int)
        elif D == 'E':
            grid[X + 1:, :] += np.ones((Q - X - 1, Q), dtype=int)
        elif D == 'W':
            grid[:X, :] += np.ones((X, Q), dtype=int)

    grid = grid.transpose()
    indices = np.argwhere(grid == np.max(grid))

    minx = np.min(grid)
    indices = indices[np.argwhere(grid[0] == minx)]
    indices = np.reshape(indices, (-1, 2))
    miny = np.min(indices[1])


    print('Case #{}: {} {}'.format(i, minx, miny))

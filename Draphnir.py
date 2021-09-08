import sys

import numpy as np

T, W = [int(x) for x in input().strip().split(' ')]
for _ in range(T):
    days = [1, 2, 3, 4, 5, 6]

    answers = []
    for d in days:
        print(d)
        sys.stdout.flush()
        answers.append(int(input()))

    a = [[1, 0, 0, 0, 0, 0],
         [3, 1, 0, 0, 0, 0],
         [7, 1, 1, 0, 0, 0],
         [15, 3, 1, 1, 0, 0],
         [31, 3, 1, 1, 1, 0],
         [63, 7, 3, 1, 1, 1]]

    a = np.ones((6, 6), dtype=int) + a
    b = np.array(answers, dtype=int)
    solution = np.linalg.solve(a, b)

    print(' '.join([str(int(x)) for x in np.rint(solution)]))
    sys.stdout.flush()

    assert int(input()) == 1

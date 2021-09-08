T = int(input())
for i in range(1, T + 1):
    N = input()

    indices = []
    for idx, c in enumerate(N):
        if c == '4':
            indices.append(idx)

    if len(indices) == 0:
        N = list(N)
        if N[0] == '1' and N[1] != '9':
            A = '9' + '0'*(len(N)-2)
            B = N[1:]
            B[0] = str(int(B[0]) + 1)
            B = "".join(B)
        else:
            last_nonzero = [i for i, c in enumerate(N) if c != '0'][-1]
            A = N.copy()
            A[last_nonzero] = str(int(N[last_nonzero]) - 1)

            A = ''.join(A)

            B = ['0'] * len(N)

            B[last_nonzero] = '1'
            B = B[last_nonzero:]
            B = ''.join(B)
    else:
        A = N.replace('4', '3')
        B = ['0'] * len(N)
        for idx in indices:
            B[idx] = '1'

        B = B[indices[0]:]
        B = ''.join(B)

    print('Case #{}: {} {}'.format(i, A, B))

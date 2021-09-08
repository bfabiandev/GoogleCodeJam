import sys

T, N, M = [int(x) for x in input().strip().split(' ')]
for _ in range(T):
    modulos = []
    coprimes = [5, 7, 9, 11, 13, 16, 17]
    for coprime in coprimes:
        print(' '.join([str(coprime) for _ in range(18)]))
        sys.stdout.flush()
        res = [int(x) for x in input().strip().split(' ')]
        modulos.append(sum(res) % coprime)

    for i in range(0 + modulos[-1], M+1, 17):
        wrong = False
        for idx, coprime in enumerate(coprimes):
            if i % coprime != modulos[idx] % coprime:
                wrong = True
                break
        if not wrong:
            print(i, sep=' ')

    sys.stdout.flush()
    assert int(input()) == 1
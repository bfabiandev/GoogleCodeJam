class Struct:
    def __init__(self, i):
        self.Cs = []
        self.Ds = []
        self.i = i

    def is_fair(self, K):
        return abs(max(self.Cs) - max(self.Ds)) <= K

    def __hash__(self):
        return hash(self.i)


T = int(input())

for t in range(1, T + 1):
    N, K = [int(k) for k in input().strip().split(' ')]

    Cs = [int(k) for k in input().strip().split(' ')]
    Ds = [int(k) for k in input().strip().split(' ')]

    n_ffs = 0

    table = [Struct(i) for i in range(N)]

    for l in range(0, N):
        table[l] = Struct(l)
        table[l].Cs.append(Cs[l])
        table[l].Ds.append(Ds[l])
        if table[l].is_fair(K):
            n_ffs += 1

        for r in range(l + 1, N):
            table[r].Cs = table[r - 1].Cs
            table[r].Ds = table[r - 1].Ds

            table[r].Cs.append(Cs[r])
            table[r].Ds.append(Ds[r])
            if table[r].is_fair(K):
                n_ffs += 1

    print('Case #{}: {}'.format(t, n_ffs))

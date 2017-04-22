import networkx as nx

T = int(input())
for i in range(1, T + 1):
    [N, Q] = [int(i) for i in input().split()]
    horses = []
    for _ in range(N):
        [E, S] = [int(i) for i in input().split()]
        horses.append([E, S])
    mat = []
    for _ in range(N):
        row = [int(i) for i in input().split()]
        mat.append(row)
    questions = []
    for _ in range(Q):
        [U, V] = [int(i) for i in input().split()]
        questions.append([U, V])

    G1 = nx.DiGraph()
    for j in range(N):
        for k in range(N):
            if mat[j][k] != -1:
                G1.add_edge(j, k, length=mat[j][k])

    lengths = nx.all_pairs_dijkstra_path_length(G1, weight='length')
    G2 = nx.DiGraph()
    for j in range(N):
        for k in range(N):
            if j in lengths:
                if k in lengths[j]:
                    if lengths[j][k] <= horses[j][0]:
                        G2.add_edge(j, k, length=lengths[j][k]/horses[j][1])

    times = nx.all_pairs_dijkstra_path_length(G2, weight='length')
    print("Case #{}: ".format(i), end='')
    for q in questions:
        print(times[q[0]-1][q[1]-1], end=' ')
    print()
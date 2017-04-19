import networkx as nx
import math
import matplotlib.pyplot as plt


def minmax(gram, p_size):
    high = math.floor(p_size / (0.9*gram))
    low = math.ceil(p_size / (1.1*gram))
    return [x for x in range(low, high+1)]

T = int(input())
for i in range(1, T + 1):
    [N, P] = [int(i) for i in input().split()]
    R = [int(i) for i in input().split()]
    Q = []
    for j in range(N):
        row = [int(i) for i in input().split()]
        row.sort()
        Q.append(row)

    G = nx.DiGraph()
    G.add_node('SOURCE')
    G.add_node('SINK')
    for j, gram in enumerate(Q[0]):
        G.add_edge('SOURCE', "{}-{}".format(gram, j), capacity=1)
    for rid in range(N-1):
        for cid1 in range(P):
            poss1 = minmax(R[rid], Q[rid][cid1])
            for cid2 in range(P):
                poss2 = minmax(R[rid+1], Q[rid+1][cid2])
                if not set(poss1).isdisjoint(poss2):
                    # forward
                    G.add_edge("{}-{}".format(Q[rid][cid1], cid1), "{}-{}".format(Q[rid + 1][cid2], cid2), capacity=1)

    for cid in range(P):
        if minmax(R[-1], Q[-1][cid]):
            G.add_edge("{}-{}".format(Q[-1][cid], cid), 'SINK', capacity=1)

    result = nx.maximum_flow(G,'SOURCE', 'SINK')[0]

    if i == 25:
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        edge_labels = nx.draw_networkx_edge_labels(G, pos)
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
        plt.draw()
        plt.show()

    print("Case #{}: {}".format(i, result))

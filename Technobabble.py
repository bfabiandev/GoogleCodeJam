import networkx as nx
from networkx.algorithms import bipartite

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    G = nx.DiGraph()
    Gleft = set()
    Gright = set()
    for j in range(N):
        u, v = input().split()
        G.add_edge(u+"1", v+"2", capacity=1)
        G.add_edge('SOURCE', u+"1", capacity=1)
        G.add_edge(v+"2", 'SINK', capacity=1)
        Gleft.add(u+"1")
        Gright.add(v+"2")
    mfmc = nx.max_flow_min_cost(G, 'SOURCE', 'SINK')

    G1 = nx.DiGraph()
    for u in mfmc.keys():
        if u != 'SOURCE' and u != 'SINK':
            for v in mfmc[u].keys():
                if v != 'SOURCE' and v != 'SINK' and mfmc[u][v] == 1:
                    G1.add_edge(u, v)

    G.remove_node('SOURCE')
    G.remove_node('SINK')

    G1left, G1right = bipartite.sets(G1)
    leftDif = Gleft - G1left
    rightDif = Gright - G1right

    counter = len(leftDif) + len(rightDif)


    print("Case #{}: {}".format(i, G.number_of_edges() - G1.number_of_edges() - counter))

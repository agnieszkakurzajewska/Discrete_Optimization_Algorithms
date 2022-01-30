import networkx as nx
import matplotlib.pyplot as plt
import random
import sys

def printGraph(G, k):
    if(k<10):
        pos=nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=5)
        labels = nx.get_edge_attributes(G,'u')
        nx.draw_networkx_edge_labels(G,pos, edge_labels=labels)
        plt.show()

def H(x):
    x_to_string = ''.join(map(str, x))
    return x_to_string.count("1")

def Z(x):
    x_to_string = ''.join(map(str, x))
    return x_to_string.count("0")

def e(i):
    i_to_string = ''.join(map(str, i))
    return int(i_to_string, 2)

def randomizeU(e):
    l = max(H(e[0]), Z(e[0]), H(e[1]), Z(e[1]))
    return random.randint(1, 2**l)

def addUToEdges(G):
    for e in G.edges:
        G.add_edge(e[0], e[1], u = randomizeU(e))
    return G

k = int(sys.argv[1])
G = addUToEdges(nx.hypercube_graph(k))
printGraph(G, k)

import networkx as nx
import matplotlib.pyplot as plt
import random
import sys
import math
import numpy as np

def getK(G):
    n = G.number_of_nodes()
    k = math.log(n,2)
    return int(k)

def printGraph(G):
    
    if(getK(G)<10):
        pos=nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=5)
        labels = nx.get_edge_attributes(G,'c')
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

def randomizeC(e):
    l = max(H(e[0]), Z(e[0]), H(e[1]), Z(e[1]))
    return random.randint(1, 2**l)

def addCFToEdges(G):
    for e in G.edges:
        G.add_edge(e[0], e[1], c = randomizeC(e), f = 0)
    return G

def createGraph(k):
    k = int(k)
    G = nx.hypercube_graph(int(k))
    G = addCFToEdges(G)
    return G

def createResidualGraph(G):
    k = getK(G)
    print(k)
    Gf = nx.hypercube_graph(int(k))
    return Gf

def getHeaviestPath(G):
    s = list(G.nodes)[0]
    t = list(G.nodes)[G.number_of_nodes()-1]

    max_flow = 0
    best_path = None

    for path in nx.all_simple_paths(G, source=s, target=t):
         flow = 0
         print(path[1])
         for i in range(1, len(path)):
            flow = flow + G[path[i-1]][path[i]]['c']
            if flow>max_flow:
                max_flow = flow
                best_path = path
    
    print(best_path)
    return best_path

# main
G = createGraph(sys.argv[1])
Gf = createResidualGraph(G)
getHeaviestPath(G)

#print(list(G.nodes)[G.number_of_nodes()-1])
printGraph(G)

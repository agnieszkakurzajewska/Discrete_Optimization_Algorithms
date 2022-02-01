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

def printEdge(G, e):
    x1 = np.asarray(e[0])
    s1 = ''
    for x in x1:
        s1 = s1+str(x)
    x1 = int(s1, 2)
    x2 = np.asarray(e[1])
    s2 = ''
    for x in x2:
        s2 = s2+str(x)
    x2 = int(s2, 2)
    u = G[e[0]][e[1]]['u']
    f = G[e[0]][e[1]]['f']
    print (str(x1)+" => "+str(x2)+"  u="+str(u)+" f="+str(f))



def randomizeC(e):
    l = max(H(e[0]), Z(e[0]), H(e[1]), Z(e[1]))
    return random.randint(1, 2**l)

def addUFToEdges(G):
    for e in G.edges:
        G.add_edge(e[0], e[1], u = randomizeC(e), f = 0)
    return G

def createGraph(k):
    k = int(k)
    G = nx.hypercube_graph(int(k))
    G = addUFToEdges(G)
    return G

def createResidualGraph(G):
    k = getK(G)
    Gf = nx.hypercube_graph(int(k))

    for e in G.edges.data():
        u = G[e[0]][e[1]]['u']
        f = G[e[0]][e[1]]['f']
        if f<u and f != 0:
            Gf.add_edge(e[0], e[1], u = u, f = u-f)
            Gf.add_edge(e[1], e[0], u = u, f = u)
        if f==u:
            Gf.add_edge(e[1], e[0], u = u, f = u)
        if f==0:
            Gf.add_edge(e[0], e[1], u = u, f = u)
    return Gf

def getShortestPath(G):
    s = list(G.nodes)[0]
    t = list(G.nodes)[G.number_of_nodes()-1]
    min_flow = 0
    shortest_path = nx.shortest_path(G,source=s,target=t)

    for i in range(1, len(shortest_path)):
        flow = G[shortest_path[i-1]][shortest_path[i]]['f']

        if min_flow == 0 or flow < min_flow:
            min_flow = flow

    return min_flow, shortest_path

def updateG(G, flow, shortest_path):
    for i in range(1, len(shortest_path)):
        v1 = shortest_path[i-1]
        v2 = shortest_path[i]
        f = G[v1][v2]['f']
        u = G[v1][v2]['u']
        nx.set_edge_attributes(G, {(v1, v2): {"f": f+flow}})
    return G

def updateGf(G, Gf):
    for e in G.edges.data():
        u = G[e[0]][e[1]]['u']
        f = G[e[0]][e[1]]['f']
        if f<u and f != 0:
            Gf[e[0]][e[1]]['f']  = u-f
        if f==u and f != 0:
            Gf.remove_edge(e[0], e[1])
            Gf.add_edge(e[1], e[0], u = u, f = u)
            print("usunalem i dodalem krawedz krawedz z GF")
            print(Gf[e[0]][e[1]])
        if f==0:
            Gf[e[0]][e[1]]['f']  = u            
    return Gf
    
# main

#init
G = createGraph(sys.argv[1])
Gf = createResidualGraph(G)
i = 0
print("G: ")
for e in G.edges.data():
    print(e)
print("Gf: ")
for e in Gf.edges.data():
    printEdge(G, e)

# while (i <3):
#     flow, shortest_path  = getShortestPath(Gf)
#     print(flow)
#     print(shortest_path)
#     G = updateG(G, flow, shortest_path)
#     Gf = updateGf(G, Gf)
#     print("G: ")
#     for e in G.edges.data():
#         print(e)
#     print("Gf: ")
#     for e in Gf.edges.data():
#         print(e)
#     i = i+1
#     print("       ")

#




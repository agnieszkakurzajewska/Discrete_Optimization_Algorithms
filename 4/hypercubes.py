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
        nx.draw(G, pos, with_labels=True, node_size=5, arrowsize=3, arrowstyle='fancy')
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
    if G.has_edge(e[0], e[1]):
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
        printw(str(x1)+" => "+str(x2)+"  u="+str(u)+" f="+str(f))

def randomizeC(e):
    l = max(H(e[0]), Z(e[0]), H(e[1]), Z(e[1]))
    return random.randint(1, 2**l)

def addUFToEdges(G):
    for e in G.edges:
        G.add_edge(e[0], e[1], u = randomizeC(e), f = 0)
    return G

def createGraph(k):
    k = int(k)
    nodes = nx.hypercube_graph(int(k))
    G = nx.DiGraph()
    G.add_nodes_from(nodes)
    G.add_edges_from(nodes.edges)
    G = addUFToEdges(G)
    return G

def createResidualGraph(G):
    k = getK(G)
    nodes = nx.hypercube_graph(int(k))
    Gf = nx.DiGraph()
    Gf.add_nodes_from(nodes)
    for e in G.edges.data():
        u = G[e[0]][e[1]]['u']
        f = G[e[0]][e[1]]['f']
        if f<u and f != 0:
            Gf.add_edge(e[0], e[1], u = u, f = u-f)
            Gf.add_edge(e[1], e[0], u = u, f = f)
        if f==u:
            Gf.add_edge(e[1], e[0], u = u, f = u)
        if f==0:
            Gf.add_edge(e[0], e[1], u = u, f = u)
    return Gf

def getHeaviestPath(G):
    s = list(G.nodes)[0]
    t = list(G.nodes)[G.number_of_nodes()-1]

    max_flow = 0
    best_path = None

    for path in nx.all_simple_paths(G, source=s, target=t):
         flow = 0
         for i in range(1, len(path)):
            flow = flow + G[path[i-1]][path[i]]['f']
            if flow>max_flow:
                max_flow = flow
                best_path = path
    
    return best_path, max_flow

def getShortestPath(G):
    s = list(G.nodes)[0]
    t = list(G.nodes)[G.number_of_nodes()-1]
    min_flow = 0
    shortest_path = 0
    try:
        shortest_path = nx.shortest_path(G,source=s,target=t)
        for i in range(1, len(shortest_path)):
            flow = G[shortest_path[i-1]][shortest_path[i]]['f']

            if min_flow == 0 or flow < min_flow:
                min_flow = flow
    except Exception:
        printw("No shortest path")
    return min_flow, shortest_path

def updateG(G, flow, shortest_path):
    for i in range(1, len(shortest_path)):
        v1 = shortest_path[i-1]
        v2 = shortest_path[i]
        f = G[v1][v2]['f']
        u = G[v1][v2]['u']
        nx.set_edge_attributes(G, {(v1, v2): {"f": f+flow, "u": u}})
    return G

def printw(str):
    if sys.argv[2] == "True":
        print(str)
# main
#init
G = createGraph(sys.argv[1])
Gf = createResidualGraph(G)

printw("\nG: ")
for e in G.edges.data():
    printEdge(G, e)
printw("Gf: ")
for e in Gf.edges.data():
    printEdge(Gf, e)

i = 0
should_search_again = True
while (should_search_again):
    printw("\n")
    flow, shortest_path  = getShortestPath(Gf)
    if shortest_path != 0:
        i = i+1
        printw("The shortest path: "+str(shortest_path))
        printw("Flow in the shortest path: "+str(flow))
        G = updateG(G, flow, shortest_path)
        Gf = createResidualGraph(G)
        printw("G: ")
        for e in G.edges.data():
            printEdge(G, e)
        printw("Gf: ")
        for e in Gf.edges.data():
            printEdge(Gf, e)
        printw("")
    else:
        should_search_again = False

# flow counting
best_path, max_flow = getHeaviestPath(G)
# printw(best_path)
printw("Max flow: ")
print(max_flow)
printw(str(i)+" interations (founded paths)\n")


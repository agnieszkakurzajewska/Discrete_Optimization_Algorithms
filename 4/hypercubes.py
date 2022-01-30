from tkinter import N
import networkx as nx
import matplotlib.pyplot as plt
import random

def printGraph(G):
    nx.draw_shell(G)
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
# def makeGraphDirected(G):
#     for e in G.edges:
#         if (H(e[0]) > H(e[1])):
#             G.add_edge(e[0], e[1])
#         else:
#             G.add_edge(e[1], e[0])
#     return G

k = 3
G = nx.hypercube_graph(k)
n = G.number_of_nodes()
# print(H.number_of_nodes())
b = (1, 1, 1)
G = addUToEdges(G)
print(G.edges(data=True))
# printGraph(H)

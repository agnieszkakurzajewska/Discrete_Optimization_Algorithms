import sys
import traceback
import logging

def set_data():

    global if_directed
    global n            #number of vertices
    global m            #number of edges
    global edges        #egdes array

    if sys.argv[1] in {"D", "d"}:
        if_directed = True
    elif sys.argv[1] in {"U", "u"}:
        if_directed = False

    n = int(sys.argv[2])
    m = int(sys.argv[3])

    edges = [[0 for j in range(2)] for k in range(m)] 

    argv_counter = 4;
    for i in range(m):
        edges[i][0] = int(sys.argv[argv_counter])
        edges[i][1] = int(sys.argv[argv_counter+1])

        argv_counter+=2

    print("Directed graph") if if_directed else print("Unirected graph")
    print("Nodes' number: ", n)
    print("Edges' number: ", m)
    print("Edges: ", edges)

def dfs(prev_node, node):

    if node not in visited_nodes:
        visited_nodes.append(node)
        add_edge(prev_node, node)
        neighbour = []
        for e in edges:
            if node == e[0]:
                neighbour.append(e[1])
            elif node == e[1] and not if_directed:
                neighbour.append(e[0])

        for n in neighbour:
            dfs(node, n)

def add_edge(prev_node, node):
    new_edge = [prev_node, node]
    revert_new_edge = [node, prev_node]

    if new_edge in edges or (revert_new_edge in edges and not if_directed):
        visited_edges.append(new_edge)
    

try:
    set_data()
except Exception as e:
    print("Invalid args!")
    sys.exit()

global visited_nodes, visited_edges
visited_nodes = []
visited_edges = []
dfs(1,1)

print("Visited nodes: ", visited_nodes)
print("Visited edges: ", visited_edges)


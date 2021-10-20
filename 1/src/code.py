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
    for i in range(0, 2*m-3):
        edges[i][0] = sys.argv[argv_counter]
        edges[i][1] = sys.argv[argv_counter+1]

        argv_counter+=2

    print(if_directed)
    print(n)
    print(m)
    print(edges)



try:
    set_data()
except Exception as e:
    print("Invalid args!")
    sys.exit()


# (DAG) (Single-source shortest paths in Directed Acyclic Graphs)

# Nicolas Perez Pando, C-212

# Execute Time: O(|E(G)| + |V(G)|)

def Relax(u, v, w):
    if d[v] > d[u] + w(u, v):
        d[v] = d[u] + w(u, v)

def Initilize_Single_Source(G, x):
    for v in vertex(G):
        d[v] = maxValue
        pi[v] = None
    d[x] = 0

def Print_Path(G, s, v):
    path = [v]
    while s != v:
        if pi[v] == None:
            print("No path from " + s + "to " + v + "exist")
            return
        path.insert(0, pi[v])
        v = pi[v]

    path.insert(0, s)
    print(path)

def DAG_Shortest_Path(G, source, w):
    x = Topological_Sort(G) # codigo que ya fue enviado en una ocacion. O(|E(G)| + |V(G)|)
    Initilize_Single_Source(G, source) #O(|V(G)|)
    for u in x:
        for v in adj(u):
            Relax(u, v, w)

def Main(G, source, target, w): # this is the main function
    pi = [None] * len(vertex(G))
    d  = [None] * len(vertex(G))

    DAG_Shortest_Path(G, source, w)
    Print_Path(G, source, target)

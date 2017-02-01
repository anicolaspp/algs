# Bellman_Ford Algoritmn

# Nicolas Perez Pando, C-212

# Execute Time: O(|V(G)| * |E(G)|)

maxValue = 10**1000000 #something like infinite

def Relax(u, v, w):
    if d[v] > d[u] + w(u, v):
        d[v] = d[u] + w(u, v)

# O (|E(G)|)
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


# we can make this method using Matrix Cost representation, but the execute time is biger

def Bellman_Ford_Adj_List(G, source, w):
    Initilize_Single_Source(G, source)

    for i in xrange(len(vertex(G)) - 1):
        for edge in edges(G):
            Relax(edge.Source, edge.Target, w)

    for edge in edges(G):
        if d[edge.target] > d[edge.Source] + w(edge):
            return False

    return True


def Main(G, source, target, w): # this is the main function
    pi = [None] * len(vertex(G))
    d  = [None] * len(vertex(G))

    if Bellman_Ford_Adj_List(G, so, w) == True: # existe el camino
        Print_Path(G, source, target)




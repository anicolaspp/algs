# Topological Sort Algoritmn

# Nicolas Perez, C-212

count = 0
result = [] # The result of Topological_Sort

def Topological_Sort(graph):
    for vertex in get_Vertex(graph):
        if vertex.Visited == False:
            DFS(vertex)

    return result

def DFS(v):
    v.Visited = True
    for child in childrens(x):
        if child.Visited == False:
            DFS(child)
    v.P = count
    result.insert(0, v)
    count += 1

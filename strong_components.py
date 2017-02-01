def InvertGraph(G):
    result = list();
    for u,v in V(G):
        result.append((v,u));
    return result;

def get_Max(lista):
    x = 0;
    for i in lista:
        if x < i:
            x = i;
    return x;

def DFS(G, x, count):
    visited[x] = True;
    for v in Ady(x):
        if not visited[v]:
            DFS(G, v, count);
    values[v] = count;
    count += 1;


def Strong_Components(G):
    values = [len(vertex(G))];
    DFS(G, get_Max(values), 0);

    Gt = InvertGraph(G);
    DFS(Gt, get_Max(values), 0);


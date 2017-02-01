# Algoritmo para hallar los puntos de articulacion
#Nicolas Perez C-212

#aqui asuminos que existe la funcion hijos(x)

count = 0

def DFS(x):
    if x.IsRoot == True and len(hijos(x)) > 1:
        yield x

    x.Profundidad = count
    count += 1
    x.Low = x.Profundidad
    x.Visited = True

    # por cada hijo (item) de x
    for item in hijos(x):
        if item.Visited == False:
            DFS(item)
            x.Low = min(x.Low, item.Low)
            if (item.Low >= x.Profundidad):
                yield x # retornando x, pues es un punto de articulacion
        else:# item ya ha sido visitado, es decir, <x, item> es arista de retroceso
            x.Low = min(item.Profundidad, x.Low) # actualizando el low de x


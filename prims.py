# Prim algorithm

# O(m log n)

from heapq import heappop, heapify

maxValue = 10**1000000 #something like infinite

def Decrease_Key(heap, i, newValue):
	a[i] = newValue
	while i > 0 and a[(i - 1) / 2] > a[i]:
		a[(i - 1)/2], a[i] = a[i], a[(i-1)/2]
		i = (i - 1)/2

def Prim(vertex, t):
    pi = []

    for i in range(len(vertex)):
        pi.append(None)

    # "Distance" is the minimum distance between vertex x and the MST
    t.Distance = 0

    heapify(vertex) #this is O( len(vertex) ) as Build_Heap(vertex)
    while len(vertex) > 0:
        x = heappop(vertex)

        for v in adyacentes(x):
            if vertex.__contains__(v) == True and cost(x, v) < v.Distance:
                pi[v.Indentifier] = x.Identifier

                # Change the value of the v.Distance and Decrease_Key into the heap (vertex)
                Decrease_Key(vertex, pos(v), cost(x, v))

    for v in vertex:
        if pi[v.Identifier] != None:
            yield (v.Identifier, pi[v.Identifier]) #return edges of MST, the edges have a form : <v.Identifier, pi[v.Identifier]>


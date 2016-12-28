class myqueue(list):
    def __init__(self,a=[]):
        list.__init__(self,a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self,x):
        self.append(x)

class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):         # voor afdrukken
        return str(self.data)

    def __lt__(self, other):    # voor sorteren
        return self.data < other.data

import math
INFINITY = math.inf # float("inf")

def vertices(G):
    return sorted(G)

def edges(G):
    return [(u,v) for u in vertices(G) for v in G[u]]

v = [Vertex(i) for i in range(8)]

G = {v[0]:[v[4],v[5]],
     v[1]:[v[4],v[5],v[6]],
     v[2]:[v[4],v[5],v[6]],
     v[3]:[v[7]],
     v[4]:[v[0],v[1],v[2],v[5]],
     v[5]:[v[1],v[2],v[4]],
     v[6]:[v[1],v[2]],
     v[7]:[v[3]]}


print("vertices(G):",vertices(G))
print("edges(G):",edges(G))

def clear(G):
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v,e)

def BFS(G,s):
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    q = myqueue()
    q.enqueue(s)
#    print("q:", q)
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY: # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)
#        print("q:", q)
print("BFS here")
BFS(G,v[1])

def show_tree_info(G):
    print('tree:', end = ' ')
    for v in vertices(G):
        print('(' + str(v), end = '')
        if hasattr(v,'distance'):
            print(',d:' + str(v.distance), end = '')
        if hasattr(v,'predecessor'):
            print(',p:' + str(v.predecessor),  end = '')
        print(')', end = ' ')
    print()

show_tree_info(G)

def is_connected(G):
    V = vertices(G)
    BFS(G, V[0])
    V = vertices(G)
    for v in V:
        if v.distance == INFINITY:
            return False
    return True

print("Is it connected:", is_connected(G))

def show_sorted_tree_info(G):
    print('sorted tree:')
    V = vertices(G)
#    V = [v for v in V if hasattr(v,'distance') and hasattr(v,'predecessor')]
    V.sort(key = lambda x: (x.distance,x.predecessor))
    d = 0
    for v in V:
        if v.distance > d:
            print()
            d += 1
        print('(' + str(v) + ',d:' + str(v.distance) + ',p:'
                                                + str(v.predecessor),  end = '')
        print(')', end = ' ')
    print()

#show_sorted_tree_info(G)

def path_BFS(G,u,v):
    BFS(G,u)
    a = []
    if hasattr(v,'predecessor'):
        current = v
        while current:
            a.append(current)
            current = current.predecessor
        a.reverse()
    return a

print("path_BFS(G,v[1],v[7]):",path_BFS(G,v[1],v[7]))

def no_cycles(G):
    V = vertices(G)
    for s in V:
        s.predecessor = None
        s.distance = 0
        for v in V:
            if v != s:
                v.distance = INFINITY  # v krijgt het attribuut 'distance'
        q = myqueue()
        q.enqueue(s)
    #    print("q:", q)
        while q:
            u = q.dequeue()
            l = []
            for v in G[u]:
                if u.predecessor != v:
                    l.append(v)
            for v in l:
                if v.distance == INFINITY: # v is nog niet bezocht
                    v.distance = u.distance + 1
                    v.predecessor = u  # v krijgt het attribuut 'predecessor'
                    q.enqueue(v)
                else:
                    return False
    return True

def get_bridges(G):
    result = []
    dummyG = G
    E = edges(dummyG)
    V = vertices(dummyG)
    for edge in E:
        dummyG[edge[0]].remove(edge[1])
        dummyG[edge[1]].remove(edge[0])
        BFS(dummyG, edge[0])
        if edge[1].distance == INFINITY:
            result.append(edge)
        dummyG[edge[0]].append(edge[1])
        dummyG[edge[1]].append(edge[0])
    return result

graaf = {v[0]: [v[1], v[3]],
         v[1]: [v[0], v[2]],
         v[2]: [v[1], v[3], v[4]],
         v[3]: [v[0], v[2]],
         v[4]: [v[2], v[5], v[6]],
         v[5]: [v[4], v[6]],
         v[6]: [v[4], v[5], v[7]],
         v[7]: [v[6]]}
show_tree_info(graaf)
print("graaf heeft geen cycles:", no_cycles(graaf))

print(get_bridges(graaf))

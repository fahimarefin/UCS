from queue import PriorityQueue, LifoQueue
from collections import defaultdict


class Element:

    def __init__(self, n, d, e):
        self.node = n
        self.distance = d
        self.edge = e

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __eq__(self, other):
        return self.edge == other.edge


dest = {}
vis = {}
final_vis = []
adj = defaultdict(list)
adjw = defaultdict(list)
dijsktra_traversal = []
prev = {}
pq = PriorityQueue()


def dijsktra(src, des, node):
    dest[src] = 0
    for i in range(1, node + 1):
        if i != src:
            dest[i] = 9999999999
        vis[i] = 0
        prev[i] = i

    pq.put(Element(src, 0,True))
    counter = 0

    while not pq.empty():
        u = pq.get()
        if u.node == des:
            break

        dijsktra_traversal.append(u.node)
        if vis[u.node] == True:
            continue
        counter = counter + 1

        vis[u.node] = True

        for i in range(0, len(adj[u.node])):
            v = adj[u.node][i]
            w = adjw[u.node][i]

            if dest[u.node] + w < dest[v]:
                dest[v] = dest[u.node] + w
                prev[v] = u.node
                pq.put(Element(v, dest[v],True))

    print(dest[des])
    roots = []
    unreachable = False
    path = LifoQueue()
    while des != src:
        if des == -1:
            unreachable = True
            break

        path.put(des)
        des = prev[des]
    if not unreachable:
        print(path.qsize() + 1)
        print(src)
        while not path.empty():
            top = path.get()
            roots.append(top)
            print(top)
    else:
        print(-1)
    print(counter)


if __name__ == "__main__":
    node, edge = map(int, input().split())

    for i in range(edge):
        u, v, w, = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        adjw[u].append(w)
        adjw[v].append(w)
    src, des = map(int, input().split())
    dijsktra(src, des, node)

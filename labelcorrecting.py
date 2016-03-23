from collections import defaultdict
from heapq import *
from collections import OrderedDict
from operator import itemgetter


edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

dist = {
	"A" : 0,
	"B" : float("inf"),
	"C" : float("inf"),
	"D" : float("inf"),
	"E" : float("inf"),
	"F" : float("inf"),
	"G" : float("inf"),
}
pred = {}



def labelc(edges, f, t):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))
    q, seen = [(0,f,())], set()
    visited = {}
    while q:
         (cost,v1,path) = heappop(q)
         if v1 not in seen:
            seen.add(v1)
            visited[v1] = cost
            d = OrderedDict(sorted(visited.items(), key=itemgetter(1)))
            path = (v1, path)
            if v1 == t: return (cost, path)
            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    if dist[v1] + c < dist[v2]:
                       dist[v2] = dist[v1] + c
                    heappush(q, (cost+c, v2, path))

    return float("inf")

print labelc(edges, "A", "G")
print dist
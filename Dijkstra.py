from collections import defaultdict
from heapq import *
from collections import OrderedDict
from operator import itemgetter

def dijkstra(edges, f, t):
    print "Staaart",f
    print "to get to",t
    g = defaultdict(list)
    print "deaffffffffffffffffffffffffault dict createdddddddddddddd"
    print g
    for l,r,c in edges:
        g[l].append((c,r))
        print "/////////////appending in default dict///////////////////////"
        print g.items()
    print "///////////////final dict///////////////",g.items()
    q, seen = [(0,f,())], set()
    visited = {}
    while q:
         print "++++++++++++++++++=before pop+++++++++++++++++++++++=",q
         (cost,v1,path) = heappop(q)
         print "-----------------------------------------------after pop------------------",q
         print "////////////COst:///////////////",cost
         print  "////////////////v1////////////:",v1
         print "///////////////////////////////path///++++++++++:",path
         if v1 not in seen:
            seen.add(v1)
            visited[v1] = cost
            d = OrderedDict(sorted(visited.items(), key=itemgetter(1)))
            print d
            print "add unvisited nodes",v1
               
            print "//////////////before path",path
            path = (v1, path)
            print "/////////////////////after path",path
            if v1 == t: return (cost, path)
            print "////////////////g.get(v1/A,())////////////////////",g.get(v1,())
            for c, v2 in g.get(v1, ()):
                print "addddddddditional cooooooooooooooooooost",c
                if v2 not in seen:
                    heappush(q, (cost+c, v2, path))

    return float("inf")

if __name__ == "__main__":
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

    print "=== Dijkstra ==="
    print edges
    print "A -> E:"
    print dijkstra(edges, "A", "E")
    print "A -> G:"
    print dijkstra(edges, "A", "G")

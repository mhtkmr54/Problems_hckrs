from collections import defaultdict
from heapq import *

edges = []
nodes = []

def prim(edges,start):
  print edges
  print start
  g = defaultdict(list)
  for l,r,c in edges:
        g[l].append((c,r))
        g[r].append((c,l))
  print g.items()
  visited =[]
  parent = {}
  key = {}
  for i in range(len(g.items())):
    parent[g.items()[i][0]] = None
    key[g.items()[i][0]] = float("inf")
  q = [(0,start)]
  print parent
  print key
  visited.append(start)
  key[start] = float("inf")
  while (q):
    print "qqqqqqqqqqqqq",q
    cost,v1 = heappop(q)
    print cost,v1
    _min = float("inf")
    pushnode = ""
    print "cost, " ,cost, "v1 the CURRRRRRRRRRRent Node",v1
    for c, v2 in g.get(v1, ()):
      if v2 not in visited and c < key[v2]:
        key[v2] = c
        parent[v2] = v1
    for el in key.keys():
        if el not in visited:
          temp = key.values()[key.keys().index(el)]
          if temp < _min:
            _min = temp
    pushnode = key.keys()[key.values().index(_min)]
    print "ey.values()",key
    print "parent.keys()",parent.keys()
    print "visited",visited
    print "pushnode",pushnode
    if v1 == "":
      return cost
    if pushnode not in visited:
      visited.append(pushnode)
      print "heappush", cost,"+",key[pushnode]," ->",cost+key[pushnode], pushnode
      heappush(q, (cost+key[pushnode], pushnode))

  #return cost


def main():
    N, M = map(int, raw_input().strip().split())
    for i in xrange(M):
        s, d , e = map(str, raw_input().strip().split())
        ed = int(e)
        edges.append((s,d,ed))
    Start = map(str, raw_input().strip().split())
    Source = Start[0]
    prim(edges, Source)

if __name__ == '__main__':
    main()

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
  for i in range(length(g.items())):
    parent[g.items()[i][0]] = None
    key[g.items()[i][0]] = float("inf")
  q, seen = [(0,start)], set()
  print parent
  print key
  while (q):
    cost,v1 = heappop(q)
    _min = float("inf")
    pushnode = ""
    for c, v2 in g.get(v1, ()):
      if v2 not in visited and c < key[v2]:
        key[v2] = c
        parent[v2] = v1
      if c < _min and v2 not in visited:
        _min = c
        pushnode = v2
        heappush(q, (cost+c, pushnode))
  return cost




def main():
    N, M = map(int, raw_input().strip().split())
    for i in xrange(M):
        s, d , e = map(str, raw_input().strip().split())
        ed = int(e)
        edges.append((s,d,ed))
    Start = map(str, raw_input().strip().split())
    prim(edges, Start)

if __name__ == '__main__':
    main()

from collections import defaultdict
from collections import OrderedDict
from operator import itemgetter
#for c, v2 in g.get(v1, ()):

def main():
    N, E = map(int, raw_input().strip(" ").split())
    g = defaultdict(list)
    nodelist = []
    for i in xrange(E):
        nodelist.append(map(int, raw_input().strip().split()))
    print nodelist
    for a, b in nodelist:
        g[a].append(b)
        g[b].append(a)
    print g.items()


if __name__ == '__main__':
    main()

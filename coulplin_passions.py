# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
#from heapq import *
#from collections import OrderedDict
#from operator import itemgetter
#if list(set(passion).intersection(d1[4:])).__len__() >= 0:

passion = []
Guest = []
candidateD = []
verpassion = defaultdict(int)

G =int(raw_input())
for i in xrange(G):
    Y = map(str,raw_input().split(" "))
    for el in Y[1:]:
      passion = list(set(passion).union([el]))

print passion

D =int(raw_input())
for el in xrange(D):
    d1 = map(str,raw_input().split(" "))
    for el in d1[4:]:
      if el in passion:
        verpassion[el] += 1
        candidateD.append(d1[0:3])


print candidateD
print passion
print verpassion

from collections import defaultdict
from collections import OrderedDict
from operator import itemgetter
import numpy as np





def poper(k,X,Y,su,ch,cv):
  global sumc
  sumc = su
  global cnth
  cnth = ch
  global cntv
  cntv = cv
  ax = np.array(X)
  print "AAAAAAAAAAAAAAAXXXXXXXXXXX",ax
  ay = np.array(Y)
  print "AAAAAAAAAAAAYYYYYYYYYYYYYYYYY",ay
  for iz in xrange(len(np.where(ay == k[0])[0])):
     cnth += 1
     print "horrrrrrrrrrizzzzzzzzatal cuts",cnth
     sumc  += k[0] * (cntv) + k[0]
     print "//////////",sumc 
  for izz in xrange(len(np.where(ax == k[0])[0])):
     cntv += 1
     print "verticllllllllllll cuts",cntv
     sumc += k[0] * (cnth) + k[0]
     print "///////////////ffffffffffffffffffffff",sumc



def genmain(s,h,v):
    global sumc
    sumc = s
    global cnth
    cnth = h
    global cntv
    cntv = v
    T =int(raw_input())
    for i in xrange(T):
       M, N = map(int, raw_input().strip().split())
       Y = map(int,raw_input().split(" "))
       X = map(int,raw_input().split(" "))
    siri = Y + X
    dsiri = defaultdict(int)

    for el in siri:
      dsiri[el] += 1

    osiri =OrderedDict(sorted(dsiri.items())) 
    print X
    print Y
    print osiri


    for pointer in reversed(range(0,len(osiri))):
       print pointer
       k = osiri.items()[pointer]
       poper(k,X,Y,sumc,cnth,cntv)

    print "maaaaaaiiiin",sumc
  
sumc = 0 
cntv = 0
cnth = 0

genmain(sumc,cnth,cntv)

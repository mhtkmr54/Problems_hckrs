from collections import defaultdict
from collections import OrderedDict
from operator import itemgetter

wrong = defaultdict(int)
right = defaultdict(int)

def getcost(X,U,cost):
   sumc  = 0
   sumg   = 0
   for k in X:
     wrong[k] += 1
   for z in U:
     right[z] += 1
   #print wrong
   #print right
   glt = OrderedDict(sorted(wrong.items()))
   shi = OrderedDict(sorted(right.items()))
   #print glt
   #print shi
   #print cost
   if  len(glt) < len(shi):
      #print "len(glt) < len(shi):"
      for p in xrange(len(shi)-len(glt),len(shi)):
          sumg += right.values()[p]
          sumc = sumg*cost[1]
      for lefti in xrange(0,len(shi)-len(glt)):
          if shi.keys()[lefti] == glt.keys()[lefti] and shi.values()[lefti]-glt.values()[lefti] > 0:
                sumc  = sumc + abs(shi.values()[lefti]-glt.values()[lefti])*cost[1]
                print sumc   
          elif shi.keys()[lefti] == glt.keys()[lefti] and shi.values()[lefti]-glt.values()[lefti] < 0:
                sumc = sumc + abs(shi.values()[lefti]-glt.values()[lefti])*cost[0]
                print sumc
          elif shi.keys()[lefti] != glt.keys()[lefti]:
                kons =  glt.values()[lefti] - shi.values()[lefti]
                if kons < 0:
                   sumc = sumc + abs(kons)*cost[1] + glt.values()[lefti]*cost[2]
                else:
                   sumc = sumc + abs(kons)*cost[0] + shi.values()[lefti]*cost[2]
                   print sumc

   elif len(glt) > len(shi):
      #print "len(glt) > len(shi):"
      for p in xrange(len(glt)-len(shi),len(glt)):
          sumg += glt.values()[p]
          sumc = sumg*cost[0]
      for lefti in xrange(0,len(shi)-len(glt)):
          if shi.keys()[lefti] == glt.keys()[lefti] and shi.values()[lefti]-glt.values()[lefti] > 0:
                sumc  = sumc + abs(shi.values()[lefti]-glt.values()[lefti])*cost[1]
                print sumc
          elif shi.keys()[lefti] == glt.keys()[lefti] and shi.values()[lefti]-glt.values()[lefti] < 0:
                sumc = sumc + abs(shi.values()[lefti]-glt.values()[lefti])*cost[0]
                print sumc
          elif shi.keys()[lefti] != glt.keys()[lefti]:
                kons =  glt.values()[lefti] - shi.values()[lefti]
                if kons < 0:
                   sumc = sumc + abs(kons)*cost[1] + glt.values()[lefti]*cost[2]
                else:
                   sumc = sumc + abs(kons)*cost[0] + shi.values()[lefti]*cost[2]
                   print sumc
                  
   elif len(glt) == len(shi):
      for lefti in xrange(0,len(shi)):
          #print "lllllleft i",lefti
          if shi.keys()[lefti] == glt.keys()[lefti] and shi.values()[lefti]-glt.values()[lefti] > 0:
                sumc  = sumc + abs(shi.values()[lefti]-glt.values()[lefti])*cost[1]
                print sumc
          elif shi.keys()[lefti] == glt.keys()[lefti] and shi.values()[lefti]-glt.values()[lefti] < 0:
                sumc = sumc + abs(shi.values()[lefti]-glt.values()[lefti])*cost[0]
                print sumc
          elif shi.keys()[lefti] != glt.keys()[lefti]:
                kons =  glt.values()[lefti] - shi.values()[lefti]
                if kons < 0:
                   sumc = sumc + abs(kons)*cost[1] + glt.values()[lefti]*cost[2]
                else:
                   sumc = sumc + abs(kons)*cost[0] + shi.values()[lefti]*cost[2]
                   print sumc

def main():
    T = input()
    for i in xrange(T):
        X = list(raw_input())
        U = list(raw_input())
        s = raw_input()
        cost = map(int,s.split(" "))
        getcost(X,U,cost)
        

if __name__ == '__main__':
    main()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import factorial
#print factorial(1000)
T = int(raw_input())

arr = []
poss_arr = []
for i in xrange(0,T):
    arr.append(int(raw_input()))
#print arr

def possiblities(N):
    #print "possiblities with N = ", N
    max_hor_set = N//4
    #print "max_hor_set",max_hor_set
    arrangements = 0
    for s in xrange(0,max_hor_set+1):
        num = N - (s * 4) + s
        arrangements += factorial(num)/(factorial(num-s) * factorial(s))
        #print "arrangements", arrangements
    poss_arr.append(arrangements)        
        

for j in arr:
    arrangements = possiblities(j)
    #print poss_arr
    
for k in poss_arr:
    lists = range(2, k+1)
    # print lists
    for p in lists:
        first = int(lists.index(p) + 1)
        #print "first", first
        for num in lists[first: -1]:
            if num % p == 0:
                lists.remove(num)
    #print lists
    print len(lists)

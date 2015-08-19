N,K,Q = map(int,raw_input().strip().split())

print N
print K
print Q




array = map(int,raw_input().strip().split())

print array

query = [None]*Q

for i in xrange(Q):
    query[i] = int(raw_input())

print query

       
def rotate(array):
  print "////////////////input array/////////////////////////"
  print array
  mirror = [None]*N
  print mirror
  for i in xrange(N-1):
    print i
    mirror[i+1] = array[i]
    mirror[0] = array[N-1]
    print mirror
    
  print mirror
  print  "//////rotaaaaaaaaaaated////////////////////"
  array  = mirror
  print "///////////array///////////////////////"
  print array
  return array 
 
for i in xrange(K):
  print i
  array = rotate(array)
  print array 

for i in xrange(len(query)):
  print array[query[i]]  





 

  

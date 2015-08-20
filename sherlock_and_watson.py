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
  mirror = [None]*N
  for i in xrange(N-1):
    mirror[i+1] = array[i]
    mirror[0] = array[N-1]
    
  array  = mirror
  return array 
 
for i in xrange(K):
  array = rotate(array)

for i in xrange(len(query)):
  print array[query[i]]  





 

  

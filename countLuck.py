n = raw_input()
for i in xrange(n):
  r,c = map(int,raw_input.strip().split())
  d = []
  for  i in xrange(r):
    matrix = d.append(raw_input.strip().split())
    

#             for i in xrange(N):
#		for j in xrange(M):
#			if matrix[i][j] == 'M':
#				he = (i, j)
#			elif matrix[i][j] == '*':
#				fe = (i, j)
#               gettttttttttttttttttt the  index


def findexit(k):
for i in range(0,2):
      if 4 not in k[i]:
         print "no da"
      else:
         print "yes"
         l = k[i].index(4)
         print "exit at",i,l
         
         return i,l



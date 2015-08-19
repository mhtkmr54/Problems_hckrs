n = raw_input()
for i in xrange(int(n)):
   N, M = map(int, raw_input().split(' '))
   matrix = []
   for i in xrange(N):
      matrix.append(raw_input())
      print matrix

K = raw_input()

for i in xrange(N):
  for j in xrange(M):
       
       if matrix[i][j] == 'M':
         he = (i, j)
       elif matrix[i][j] == '*':
         fe = (i, j)

print he
print fe


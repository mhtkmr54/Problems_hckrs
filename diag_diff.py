N = int(raw_input())
a = []
for k in xrange(N):
  a.append((raw_input().split(" ")))

print a

diag1 = []
diag2 = []

for i in xrange(N):
  for j in xrange(N):
    if i == j:
      diag1.append(a[i][j])

print diag1

sum1 = 0
sum2 = 0

for ks in xrange(len(diag1)):
    sum1 = sum1 + int(diag1[ks])

print sum1 


for i in xrange(N):
  for j in xrange(N):
     if i+j == N-1:
       diag2.append(a[i][j])


print diag2

for ksa in xrange(len(diag2)):
    sum2 = sum2 + int(diag2[ksa])

print sum2

diff = 0

if sum2 > sum1:
   diff = sum2 - sum1
else:
   diff = sum1 - sum2

print diff


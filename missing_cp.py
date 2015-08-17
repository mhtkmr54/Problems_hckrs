n = int(raw_input())
xo = raw_input()
xo = xo.split()
x = map (int,xo)
d = {}
for i in x:
  if i not in d.keys():
    d[i] = i 
  else:
    d[i] = d[i]+1
n = int(raw_input())
dd = {}
xo = raw_input()
xo = xo.split()
x = map (int,xo)
for i in x:
   if i not in dd.keys():
     dd[i] = i
   else:    
     dd[i] = dd[i]+1

oo = []

for i in dd.keys():
   if dd[i] != d[i]:
     oo.append(i)

oo.sort()
print oo
for i in oo:
   print i,

   

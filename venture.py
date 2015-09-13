M = 0
print "Enter the number of positive integer"
M = int(raw_input(">"))

print "Enter the  positive integers one by one"

a=[]


for i in xrange(M):
   a.append(raw_input(">>"))

comp = []

for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if int(a[i])*10**len(a[j])+int(a[j]) > int(a[j])*10**len(a[i])+int(a[j]):
            a[i], a[j] = a[j], a[i]  #Swaping elements

print ''.join(a)

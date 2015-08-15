import random

def mergeSort(items):
  if len(items)> 1:
     mid = len(items)//2
     lh = items[:mid]
     rh = items[mid:]
     mergeSort(lh)
     mergeSort(rh)
     
     i=0
     j=0
     k=0

     while i < len(lh) and j < len(rh):
        if lh[i] < rh [i]:
           items[k] = lh[i]
           i = i +1
           print "item from lh selected"
           k = k+1
        else:
           items[k] = rh[j]
           j = j+1
           k = k+1
  
        while i < len(lh):
           items[k] = lh[i]
           i = i+1
           k = k+1
   
        while i < len(lh):
           items[k] = rh[j]
           j = j+1
           k = k+1
  print"merging",items


it = [random.randint(-30,12) for c in range(4)]
print "before:",it
mergeSort(it)
print "new :",it

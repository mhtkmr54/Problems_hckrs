import random

def insertion_sort(items):
  for i in range(1,len(items)):
    j=1
    while j>0 and items[j] < items[j-1]:
     items[j],items[j-1] = items[j-1],items[j]
     j -= 1


def mah_sort(items):
  for i in range (1,len(items)):
    temp = items[i]
    j=i
    while j>0 and items[j-1] > temp:
			      items[j] = items[j-1]
      j -= 1
    items[j] = temp

itms = [random.randint(-12,40) for c in range(5)]
print "before: ",itms
mah_sort(itms)
print "after",itms

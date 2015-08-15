import random

random_items = [random.randint(-50, 100) for c in range(32)]




def bubble_sort(items):
    """ Implementation of bubble sort """
    for i in range(len(items)):
       print "setting index"
       for j in range (len(items)-1-i):
         if  items[j]>items[j+1]:
          print "swapping....."
          items[j],items[j+1] = items[j+1],items[j] #Swap!!



print 'Before: ', random_items
bubble_sort(random_items)
print 'After : ', random_items

import random
 
	def quicksort( aList ):
    _quicksort( aList, 0, len( aList ) - 1 )
 
def _quicksort( aList, first, last ):
    if first < last:
      pivot = partition( aList, first, last )
      _quicksort( aList, first, pivot - 1 )
      _quicksort( aList, pivot + 1, last )
 
 
def partition(lst, start, end):
    pos = start                           # condition was obsolete, loop won't
                                          # simply run for empty range

    for i in range(start, end):           # i must be between start and end-1
        if lst[i] < lst[end]:             # in your version it always goes from 0
            lst[i],lst[pos] = lst[pos],lst[i]
            pos += 1

    lst[pos],lst[end] = lst[end],lst[pos] # you forgot to put the pivot
                                          # back in its place
    return pos



random_items = [random.randint(-50, 100) for c in range(10)]

print 'Before: ', random_items
quicksort(random_items)
print 'After : ', random_items

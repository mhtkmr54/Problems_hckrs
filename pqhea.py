import heapq
listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)        # for a maxheap!!
heapq.heappush(heap, item)
heapq.heappop(heap)
heapq.heappushpop(heap, item)
eapq.nlargest(n, iterable[, key])

import heapq
max_vals = heapq.nlargest(2, my_list)
index1 = my_list.index(max_vals[0])
index2 = my_list.index(max_vals[1])
print index1
print index2

from heapq import nlargest
lst = [9,1,6,4,2,8,3,7,5]
nlargest(3, lst) # Gives [9,8,7]

from heapq import nlargest
tags = [ ("python", 30), ("ruby", 25), ("c++", 50), ("lisp", 20) ]
nlargest(2, tags, key=lambda e:e[1]) # Gives [ ("c++", 50), ("python", 30) ]

 from heapq import heapify, nlargest
>>> l = [9,1,6,4,2,8,3,7,5]
>>> heapify(l)
>>> nlargest(3, l)
[9, 8, 7]

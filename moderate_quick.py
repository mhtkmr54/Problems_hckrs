# Enter your code here. Read input from STDIN. Print output to STDOUT
import random

def quicksort( aList ):
    _quicksort( aList, 0, len( aList ) - 1 )

def _quicksort( aList, first, last ):
    if first < last:
      pivot = partition( aList, first, last )
      _quicksort( aList, first, pivot - 1 )
      _quicksort( aList, pivot + 1, last )


def partition(lst, start, end):
    pivot = end                      
    pIndex = start                                      

    for i in range(start, end):           
        if lst[i] < lst[pivot]:            
            lst[i],lst[pIndex] = lst[pIndex],lst[i]
            pIndex += 1

    lst[pIndex],lst[end] = lst[end],lst[pIndex]
    out = map(str, lst)
    
    print  " ".join(out) 
                                          
    return pIndex


def main():
  raw_input()
  ints = map(int, raw_input().split(' '))
  
  quicksort( ints )
  

  return ints
  


if __name__ == '__main__':
    main()
    





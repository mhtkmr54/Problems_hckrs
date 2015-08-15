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
    print "",lst 
                                          
    return pIndex


def main():
  n = int(raw_input())
  if n == 7:
    inp = raw_input('Enter input: ')
    ints = map(int, inp.split(' '))

    return ints
  else:
    print "enter again"
    main()

intsa = main()

print 'Before: ', intsa
quicksort( intsa )
print 'After : ', intsa

if __name__ == '__main__':
    main()
    





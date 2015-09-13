import random

def merge_sort(items):
 if len(items) > 1:
   mid = len(items)/2
   left = items[0:mid]
   right = items[mid:]
   merge_sort(left)
   merge_sort(right)
   

   l,r =0,0
   

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:

        mid = len(alist)//2
        print"///////////////////////////found mid by floor div//////////////////////////////////////////"
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        print"///////////////////////////split in mid formed 2win////////////////////////////////////////"

        mergeSort(lefthalf)
        print"//////////////////left half/////////// %r" % lefthalf
        mergeSort(righthalf)
        print"//////////////////right half/////////// %r" % righthalf


        i=0
        j=0
        k=0
         

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                print "Gone baby Gone"
                i=i+1
            else:
                alist[k]=righthalf[j]
                print "genda"
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
            print "yfa"

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
            print "sdfsdf"
    print("Merging ",alist)



it = [random.randint(0,100) for c in range(5)]
print "before:",it
mergeSort(it)
print "new :",it


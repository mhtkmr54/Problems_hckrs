M = 0
print "Enter the number of positive integer"
M = int(raw_input(">"))

print "Enter the  positive integers one by one"

a=[]


for i in xrange(M):
   a.append(raw_input(">>"))



def bubble_sort(a):
 for i in range(len(a)-1):
    for j in range(i+1, len(a)):
        if int(a[i])*10**len(a[j])+int(a[j]) > int(a[j])*10**len(a[i])+int(a[j]): #the custom comparison
            a[i], a[j] = a[j], a[i]  #Swaping elements
            print ''.join(a)
   

def mergeSort(alist):
    if len(alist)>1:
        #splitting the array
        mid = len(alist)//2  #the floor div
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)  #the recursive call after splitting
        mergeSort(righthalf) #the recursive call after splitting
      
        i=0
        j=0
        k=0
         

        while i < len(lefthalf) and j < len(righthalf):

            if  int(lefthalf[i])*10**len(righthalf[j])+int(righthalf[j]) < int(righthalf[j])*10**len(lefthalf[i])+int(lefthalf[i]): #custom comparison
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):  #to be used when index j is out of range of len(righthalf)
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf): #to be used when index i is out of range of len(lefthalf)
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def main():
  print "BEFORE SORTING THE ARRAY IS:",a
  mergeSort(a)
  print "AFTER SORTING THE ARRAY IS:",a
  print "THE LEAST NUMBER is:"
  print "".join(a)

if __name__ == "__main__":
    import cProfile
    cProfile.run("main()")

import numpy

def main():
  
  na = int(raw_input())
  a = map(int, raw_input().split(' '))
  nb= int(raw_input())
  b = map(int, raw_input().split(' '))
  gen(na,a,nb,b)


  

def gen (na,a,nb,b):
  print " ",na,a,nb,b
  for i in range(len(a)):
     x = numpy.array(a)
     if len(numpy.where(x == a[i])[0]) > 0 :
         a
 
    


if __name__ == '__main__':
    main()


# Enter your code here. Read input from STDIN. Print output to STDOUT a.index(max(a))

length = raw_input()
X = map(int,raw_input().strip().split(' '))
Y = map(int,raw_input().strip().split(  ' '))
   
op = 0

inter = list(set(X).intersection(Y))

while inter:
    for el in inter:
        X.pop(X.index(el))
        Y.pop(Y.index(el))
    inter = list(set(X).intersection(Y))
          
def find_operations(X,Y,op):
    while inter:
        for el in inter:
            X.pop(X.index(el))
            Y.pop(Y.index(el))
        inter = list(set(X).intersection(Y))
    if max(X) < min(Y) or min(X) > max(Y):
        return -1
    elif max(X) > min(Y) and max(X) < max(Y) and min(X) < min(Y):
        return -1
    elif min(X) > min(Y) and min(X) < max(Y) and max(X) > max(Y):
        return -1
    elif max(X) > max(Y) and min(X) < min(Y):
        a(a.index(max(a))) -= 1
        a(a.index(min(a))) += 1
        op += 1
        find_operations(X,Y,op)
       
print find_operations(X,Y,op)
    
    
    
    

# Enter your code here. Read input from STDIN. Print output to STDOUT a.index(max(a))

length = raw_input()
X = map(int,raw_input().strip().split(' '))
Y = map(int,raw_input().strip().split( ' '))

op = 0


def find_operations(X,Y,op):
    if X == Y:
        return op
    inter = list(set(X).intersection(Y))
    #print X, "XXXXXXXXXXXXX"
    #print Y, "YYYYYYYYYYY"
    #print inter, "inter"
    while inter:
        for el in inter:
            X.pop(X.index(el))
            Y.pop(Y.index(el))
        inter = list(set(X).intersection(Y))
    #print X, "After rem inter X"
    #print Y, "After rem exter Y"
    if max(X) < min(Y) or min(X) > max(Y):
        print -1
        return -1
    elif max(X) > min(Y) and max(X) < max(Y) and min(X) < min(Y):
        print -1
        return -1
    elif min(X) > min(Y) and min(X) < max(Y) and max(X) > max(Y):
        print -1
        return -1
    elif max(X) > max(Y) and min(X) < min(Y):
        X[X.index(max(X))] -= 1
        X[X.index(min(X))] += 1
        op += 1
        if X == Y:
            print op
            return op
        else:
            find_operations(X,Y,op)
    elif max(X) < max(Y) and min(X) > min(Y):
        #print "X is short range"
        X[X.index(max(X))] += 1
        X[X.index(min(X))] -= 1
        op += 1
        #print X, "After Short to long op X"
        #print Y, "as it is Y"
        if X == Y:
            print op
            return op
        else:
            find_operations(X,Y,op)


find_operations(X,Y,op)





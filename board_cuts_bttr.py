# Enter your code here. Read input from STDIN. Print output to STD
T =int(raw_input())
for i in xrange(T):
    M, N = map(int, raw_input().strip().split())
    Y = map(int,raw_input().split(" "))
    X = map(int,raw_input().split(" "))

    Y.sort(reverse=True)
    X.sort(reverse=True)

    #print Y
    #print X

    y_cut = x_cut = 1     #To count the number of segments
    cost = i = j = 0

    while i < X.__len__() and j < Y.__len__():
        #print i
        #print "X arra", X
        #print X[i],"or", Y[j]
        if X[i] >= Y[j]:
            #print "selected X" ,X[i]
            x_cut = x_cut + 1
            cost = cost + X[i]*y_cut
            #print "cost", cost
            i = i+1
        else:
            #print "selected Y" ,Y[j]
            y_cut = y_cut + 1
            cost = cost + Y[j]*x_cut
            j = j+1
    #print "i,j"
    #print i,j

    while i < X.__len__():
        #print "selected Y len Exhausted" ,X[i]
        cost = cost + X[i]*y_cut
        i = i+1

    while j < Y.__len__():
        #print "selected X len Exhausted" ,Y[j]
        cost = cost + Y[j]*x_cut
        j = j+1

    print cost

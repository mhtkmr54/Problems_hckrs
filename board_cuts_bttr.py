# Enter your code here. Read input from STDIN. Print output to STD
T =int(raw_input())
for i in xrange(T):
    M, N = map(int, raw_input().strip().split())
    Y = map(int,raw_input().split(" "))
    X = map(int,raw_input().split(" "))

Y.sort(reverse=True)
X.sort(reverse=True)

y_cut = x_cut = 1     #To count the number of segments
cost = i = j = 0

while i < X.__len__() and j < Y.__len__():
    if X[i] >= Y[j]:
        x_cut = x_cut + 1
        cost = cost + (X[i]*y_cut)
        i = i+1
    else:
        y_cut = y_cut + 1
        cost = cost + (Y[j]*x_cut)
        j = j+1

while i < X.__len__():
    cost = cost + (X[i]*y_cut)
    i = i+1

while j < Y.__len__():
    cost = cost + (Y[j]*x_cut)
    j = j+1

print cost

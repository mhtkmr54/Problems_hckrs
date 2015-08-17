# Enter your code here. Read input from STDIN. Print output to STDOUT

dire = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def dfs(i, j, mat, mark, color):
    print "in dfs///////////////////////////////////////////////////////////////"
    print "i and j ----",i,j
    if i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]): return
    print "After 1"
    if mat[i][j] == 0: return
    print "After 2"
    if mark[i][j] != -1: return
    print "After 3"
    mark[i][j] = color
    print  "color :",color 
    for d in dire:
        dfs(i+d[0], j+d[1], mat, mark, color)
        
N = int(raw_input())
M = int(raw_input())
mat = []
for i in xrange(N):
    mat.append(map(int, raw_input().split()))
    print "",mat
print "after for loop",mat
mark = [ [-1]*M for i in xrange(N)]
print "mark is----",mark
c = 0
for i in xrange(N):
    for j in xrange(M):
        dfs(i, j, mat, mark, c)
        print "///////////////////////////////////////////OUT OF DFS//////////////////////////////"
        print "will change c"
        c += 1
        print "//////////////ccccccccccccccccccccccccccccccccccccccccccccccccc/////",c
        print "",mark


count = [0]*(N*M)
for i in xrange(N):
    for j in xrange(M):
        if mark[i][j] != -1:
            count[mark[i][j]] += 1
            
print max(count)

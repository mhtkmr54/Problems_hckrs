from collections import *

def maxflow(start,end):
    flow=0 # total flow found so far
    F=defaultdict(int) # flow (skey-symmetric)
    while 1:
        # BFS for augmenting path, only augment one at a time
        fifo=deque()
        fifo.append(start)
        R={} # Augmented nodes predecessors
        found=0
        while fifo and not found:
            x=fifo.popleft()
            for n in G_next[x]:
                if n in R: continue
                residual_cap=C[x,n]-F[x,n]
                if residual_cap>0:
                    R[n]=x
                    fifo.append(n)
                    if n==end:
                        fifo=0
                        found=1
                        break
        if not found:
            return flow
        # Now augment path
        n=end
        while n!=start:
            x=R[n]
            F[x,n]+=1
            F[n,x]-=1
            n=x
        flow+=1
                    


def addedge(a,b,cap):
    C[a,b]=cap
    print "//////////////////CAPACITY DEFAULT DICT"
    print C
    G_next[a].append(b)
    G_next[b].append(a) # needed for ford fulkerson reverse flows
    print "G_next"
    print G_next

C=input()
for c in range(C):
    N,T,M=map(int,raw_input().split())
    G_next=defaultdict(list)
    C=defaultdict(int) # capacity
    for m in range(M):
        a,b = map(int,raw_input().split())
        a-=1
        b-=1
        addedge(2*a,2*b+1,1)
        addedge(2*b,2*a+1,1)
    start=2*N
    end=2*N+1
    for a in range(N):
        addedge(start,2*a,T)
        addedge(2*a+1,end,1)
    print maxflow(start,end)


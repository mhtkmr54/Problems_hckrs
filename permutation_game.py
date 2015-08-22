
def is_increasing(p):
    print all(p[i] < p[i + 1] for i in range(len(p) - 1))
    return all(p[i] < p[i + 1] for i in range(len(p) - 1))

def remove(p, i):
    return [x if x < i else x - 1 for x in p if x != i]

def children(p):
    return (remove(p, i) for i in range(1, len(p) + 1))

def memo(f):
    m = {}
    def g(x):
        if x not in m:
            m[x] = f(x)
        return m[x]
    return g
    
@memo
def _win(p):
    return (not is_increasing(p)) and any(not win(c) for c in children(p))

def win(p):
    return _win(tuple(p))

for i in range(int(raw_input())):
    raw_input()
    print "Alice" if win(map(int, raw_input().split())) else "Bob"

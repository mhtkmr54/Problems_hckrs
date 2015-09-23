# https://www.hackerrank.com/challenges/cut-the-tree


def gen_t(v, edge):
    def add_t(t, a, b):
        if a not in t:
            t[a] = set()
            print t[a]
        t[a].add(b)
        print t[a]

    t = {}
    for a, b in edge:
        print "aading tab"
        add_t(t, a, b)
        print "adding tba"
        add_t(t, b, a)
    print t
    return t


def dfs(t, v, w, root):
    visited, visit_stack, val_stack = set(), [root], []
    while visit_stack:
        curr = visit_stack.pop()
        if curr not in visited:
            print "curr not in visited!!!!!!!!"
            visited.add(curr)
            print "so i added in visited set",visited
            print "tcurrrrrrrrrrrrr",t[curr]
            print "visited",visited
            left_childs = t[curr] - visited
            print "left cheeeeled",left_childs
            if not left_childs:
                w[curr-1] = v[curr-1]
                print "no left child"
            else:
                print "left child is there,So append curr to val stack"
                val_stack.append(curr)

                print "val_stack////////AFTER APPENDING CURR////////////////",val_stack
            visit_stack.extend(left_childs)
            print "after extending value stack",visit_stack
    for curr in reversed(val_stack):
        w[curr-1] = v[curr-1] + sum([w[i-1] for i in t[curr]])


def minimun_tree_diff(v, edge):
    t = gen_t(v, edge)
    w = [0] * len(v)
    print "wwwwwwwwwww//",w
    print "iiiiiiiiiiiiiiiiiiteeeeeeeeeeems",t.items()
    for k, val in t.items():
        print "going for  k val or should i say setting root??",k,val
        if val:
            root = k
            break
    dfs(t, v, w, root)
    total = sum(v)
    t_diff = [abs(total - val * 2) for val in w[1:]]
    return min(t_diff)

if __name__ == '__main__':
    n = input()
    v = map(int, raw_input().split())
    print v
    edge = [map(int, raw_input().split()) for i in range(n-1)]
    print edge
    print minimun_tree_diff(v, edge)

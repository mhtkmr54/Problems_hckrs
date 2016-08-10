#!/bin/python

import sys


n = int(raw_input().strip())
a = map(float,raw_input().strip().split(' '))
cut = 0
diff = 0.0 


def min_cuts(a,cut):
    if max(a) < 0.5*(sum(a)):
        return 0
    elif max(a) == 0.5*(sum(a)):
        cut += 1
        return cut
    elif max > 0.5*(sum(a)):
        oldmaxi = a.index(max(a))
        diff = (max(a) - 0.5*(sum(a)))*2
        a[a.index(max(a))] -= diff
        if a.index(max(a)) == oldmaxi:
            cut += 1
            return cut
        else:
            min_cuts(a)
            
print min_cuts(a,cut)

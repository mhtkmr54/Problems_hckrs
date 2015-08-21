#!/usr/bin/py
import numpy 
from collections import *


def lonelyinteger(a):
    k = defaultdict(int)
    for l in a:
        k[l] += 1    
    ds = [k for k, v in k.items() if v == 1]
    return ds[0] 

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)

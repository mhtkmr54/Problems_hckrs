#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
if n == 0:
    print 0
elif m > n :
    print 0
else:
    print n-m

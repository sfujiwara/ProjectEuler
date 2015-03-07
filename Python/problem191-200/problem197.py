# -*- coding: utf-8 -*-

'''
試しに走らせてみたところ, 理由はわからないが, 十分大きい N に対して
u_n + u_{n+1} = 1.710637717　for all n > N,
が成り立つらしい.
n = 10^3 で十分だった
理由は全くわからない.
'''

import math
from decimal import *

def f(x):
    return math.floor(2**(30.403243784 - x**2)) * 1e-9

if __name__ == '__main__':
    ## decimal を使わなくても精度は十分だった
    ## getcontext().prec = 10
    n = 10**3
    u_bef = -1
    for i in xrange(n+1):
        u = f(u_bef)
        ans = u + u_bef
        u_bef = u
        ## print ans
    print 'Answer:', ans

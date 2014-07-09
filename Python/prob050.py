# -*- coding: utf-8 -*-
import math
from datetime import datetime

# n以下の素数列を返す関数(エラトステネスの篩)
def get_prime(n):
    prime = [True]*(n+1)
    prime[0], prime[1] = False, False
    for i in xrange(2, int(math.sqrt(n))+1):
        if prime[i]:
            for j in xrange(i*2, n+1, i):
                prime[j] = False
    p = []
    for i in xrange(n+1):
        if prime[i]: p.append(i)
    return p

n = 1000000
prime = get_prime(n)
for i in xrange(500, 600):
    for j in xrange(len(prime)-i):
        tmp = sum(prime[j:(j+i)])
        if tmp > n: break
        if tmp in prime:
            ans = tmp
            memo = i
            print ans, memo

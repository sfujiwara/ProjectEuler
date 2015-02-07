# -*- coding: utf-8 -*-

## n の真の約数の和を返す関数
def d(n):
    divisor_sum = 0
    for i in xrange(1, n):
        if n%i == 0: divisor_sum += i
    return divisor_sum

ans = 0
for i in xrange(1, 10000):
    if i == d(d(i)) and i!= d(i):
        ans += i

print ans

# -*- coding: utf-8 -*-

from decimal import *

'''
まともにやると計算誤差でずれるので,
開平法を使って計算するはずだったが面倒なので
Decimal を使ってみた.
'''

if __name__ == '__main__':
    getcontext().prec = 110
    ans = 0
    for i in range(2, 101):
        r = Decimal(i).sqrt()
        if r % 1 != 0:
            ans += sum(int(j) for j in str(r * 10**100)[:100])
    print 'Answer:', ans

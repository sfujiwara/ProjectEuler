# -*- coding: utf-8 -*-

'''
2 つの素数を掛けあわせてできる数を調べるだけ.
'''

import math

## エラトステネスの篩でn以下の素数列を返す関数
def sieve(n):
    ## 0-nが素数か否かのフラグ
    flag = [True]*(n+1)
    ## 0, 1 は素数ではない
    flag[0], flag[1] = False, False
    for i in xrange(2, int(math.sqrt(n))+1):
        if flag[i]:
            for j in xrange(i*2, n+1, i): flag[j] = False
    return [i for i in xrange(n+1) if flag[i]]

if __name__ == '__main__':
    n = 100000000
    p = sieve(n)
    ans = 0
    for i in xrange(len(p)):
        for j in xrange(i, len(p)):
            cand = p[i] * p[j]
            if cand < n:
                ans += 1
            else:
                break
    print 'Answer:', ans

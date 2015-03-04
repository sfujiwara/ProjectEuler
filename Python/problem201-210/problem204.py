# -*- coding: utf-8 -*-

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

def count_hamming_num(p, n=1):
    if n > 10**9:
        return 0
    elif len(p) == 0:
        return 1
    else:
        return count_hamming_num(p, n*p[0]) + count_hamming_num(p[1:], n)

if __name__ == '__main__':
    primes = sieve(100)
    print 'Answer:', count_hamming_num(primes)

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

## (素数) リスト p に含まれる数を使って n を何通りに表せるか計算する関数
def ways(n, p):
    if n - p[0] < 0: return 0
    if n - p[0] == 0: return 1
    return ways(n, p[1:]) + ways(n-p[0], p)

if __name__ == '__main__':
    prime_list = sieve(1000)
    for i in range(100):
        if ways(i, prime_list) >= 5000:
            print 'Answer:', i
            break

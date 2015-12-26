# -*- coding: utf-8 -*-

'''
綺麗に書けなくて Dreamshire をカンニングしたら,
解答が完璧すぎて丸写しにしかできなかった.
やばい, マジやばい, すごい.
感動した.
'''

import math

## エラトステネスの篩でn以下の素数列を返す関数
def sieve(n):
    ## 0~nが素数か否かのフラグ
    flag = [True]*(n+1)
    ## 0, 1 は素数ではない
    flag[0], flag[1] = False, False
    for i in xrange(2, int(math.sqrt(n))+1):
        if flag[i]:
            for j in xrange(i*2, n+1, i): flag[j] = False
    return [i for i in xrange(n+1) if flag[i]]

if __name__ == '__main__':
    n = 20000000
    m = 15000000
    ans = 0
    for p in sieve(n):
        pp = p
        while pp <= n:
            ans += p * (n/pp - m/pp - (n - m)/pp)
            pp *= p
    print 'Answer:', ans

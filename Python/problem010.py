# -*- coding: utf-8 -*-
import math

# エラトステネスの篩でn以下の素数列を返す関数
def sieve(n):
    # 0-nが素数か否かのフラグ
    flag = [True]*(n+1)
    # とりあえず0, 1は素数ではない
    flag[0], flag[1] = False, False
    for i in xrange(2, int(math.sqrt(n))+1):
        if flag[i]:
            for j in xrange(i*2, n+1, i): flag[j] = False
    return [i for i in xrange(n+1) if flag[i]]

print "Answer =", sum(sieve(2000000))

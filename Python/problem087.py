# -*- coding: utf-8 -*-

'''
基本的に力ずく.
最初から集合として要素を足すよりも,
リストとして要素を足してから最後に集合に直した方が圧倒的に速い.
union の計算が遅い?
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
    prime_list = sieve(10000)
    ## ans = set([])
    ans = []
    for i in prime_list:
        for j in prime_list:
            for k in prime_list:
                cand = i**2 + j**3 + k**4
                if cand >= 5 * 10**7:
                    break
                ## ans = ans.union({cand})
                ans.append(cand)
    print 'Answer:', len(set(ans))

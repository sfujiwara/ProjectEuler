# -*- coding: utf-8 -*-

'''
約数の個数が 2 の冪乗となる数は以下のように表される.
N = 2^(2^a1 - 1) + 3^(2^a2 - 1) + 5^(2^a3 - 1) + 7^(2^a4 - 1) + ...
このとき,
a1, a2, ... のいずれかを 1 増やすと, N の約数の個数は 2 倍になる.
'''

'''
未解答.
多分数時間かければ解ける.
'''

import math
import numpy as np

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
    primes = sieve(1000000)
    a = [0] * len(primes)
    cnt = 1
    ## a[i] を 1 増やすと何倍になるかを表す配列
    costs = [primes[i]**(2**(a[i]+1) - 2**a[i]) for i in range(len(primes))]
    ind = 0
    max_ind = 1
    while cnt <= 500500:
        ## ind = min(enumerate(costs), key=lambda x: x[1])[0]
        ind = np.argmin(costs[:(max_ind+2)])
        a[ind] += 1
        max_ind = max(ind, max_ind)
        cnt += 1
        costs[ind] = primes[ind]**(2**(a[ind]+1) - 2**a[ind])
        if a[-1] != 0:
            print 'The list of prime numbers is too short'
            break

    print 'Answer:'

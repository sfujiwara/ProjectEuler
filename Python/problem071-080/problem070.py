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

def is_permutation(a, b):
    return sorted(str(a)) == sorted(str(b))

if __name__ == '__main__':
    ## 本当はどれくらいの長さの素数列が必要か考える必要あり
    p = sieve(10000)
    min_ratio = 100
    ## 相異なる 2 つの素数の積を解の候補として調べる
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            n = p[i] * p[j]
            if n > 10**7:
                break
            phi_n = (p[i]-1) * (p[j]-1)
            if is_permutation(n, phi_n):
                ratio = float(n) / phi_n
                if float(n) / phi_n < min_ratio:
                    min_ratio = ratio
                    ans = n
    ## 3 つ以上の素数の積は調べなくても良いと判定するにはどうすれば良いか後で考える
    print 'Answer:', ans   

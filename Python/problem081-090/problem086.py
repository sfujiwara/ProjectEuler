# -*- coding: utf-8 -*-

import fractions

def count_cuboids(l):
    res = 0
    for n in xrange(1, l+1):
        for m in xrange(n+1, l+1):
            if (m-n) % 2 == 1 and fractions.gcd(m, n) == 1:
                ## 原始ピタゴラス数を生成
                a, b, c = sorted([m**2-n**2, 2*m*n, m**2+n**2])
                a_prime, b_prime, c_prime = a, b, c
                ## 原始ピタゴラス数の倍数を調べる
                while a <= l and b <= 2*l:
                    if b <= l:
                        ## a はどのように分割しても良い
                        res += (a)/2
                    ## b の分割
                    res += max(0, (2*a - b + 2) / 2)
                    a += a_prime
                    b += b_prime
                    c += c_prime
    return res

if __name__ == '__main__':
    ## 予め大雑把にあたりをつけたが, 本当は二分探索などが良い
    for i in range(1800, 2000):
        if count_cuboids(i) > 10**6:
            print 'Answer:', i
            break

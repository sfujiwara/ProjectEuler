# -*- coding: utf-8 -*-

'''
x^a * y^b * z^c　の約数の和は
(x^0 + ... + x^a) ... (z^0 + ... + z^c)
と計算できる.
()の中は等比級数の和なのでまとめることができる.
'''

## n の真の約数の和を返す関数 (これは遅い)
## def d(n):
##     divisor_sum = 0
##     for i in xrange(1, n):
##         if n%i == 0: divisor_sum += i
##     return divisor_sum

## Prime Factor Decomposition
## 出力は Ruby の prime_division と同じ
## x^a * y^b * z^c -> [[x, a], [y, b], [z, c]]
def pfd(n):
    prime_factors = []
    upper_threshold = n**0.5
    ## 後のループを奇数だけで回すために, 2 だけ場合分けする
    if n % 2 == 0:
        factor = 2
        count = 0
        while n % factor == 0:
            n = n / factor
            count += 1
        prime_factors.append([factor, count])
    ## 3 以上のの素因数を探す
    factor = 3
    while n > 1:
        ## √n を超える素数は調べる必要がない
        if factor > upper_threshold:
            prime_factors.append([n, 1])
            break
        ## 割り続けて素因数 factor を取り除く
        if n % factor == 0:
            count = 0
            while n % factor == 0:
                n = n / factor
                count += 1
            prime_factors.append([factor, count])
        ## 3 以上の素数は全て奇数なので, 奇数だけ調べれば十分
        ## 本当は素数だけを調べれば十分
        factor += 2
    return prime_factors

## n の真の約数の和を返す関数
def d(n):
    if n == 0: return 0
    res = 1
    for i in pfd(n):
        res *= (i[0]**(i[1]+1) - 1) / (i[0] - 1)
    return res - n

if __name__ == '__main__':
    ans = 0
    for i in xrange(1, 10000):
        if i == d(d(i)) and i!= d(i):
            ans += i
    print ans

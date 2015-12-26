# -*- coding: utf-8 -*-

'''
三角数は n(n+1)/2 と書くことができる.
n が偶数の場合, n と (n+1)/2 は互いに素なので, 分割して素因数分解すれば良い.
n が奇数の場合は n/2 と (n+1) に分ける.
'''

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

if __name__ == '__main__':
    i = 2
    while True:
        if i % 2 == 0:
            prime_factors1 = pfd(i / 2)
            prime_factors2 = pfd(i + 1)
        else:
            prime_factors1 = pfd(i)
            prime_factors2 = pfd((i + 1) / 2)
        num_of_factors1 = 1
        for j in xrange(len(prime_factors1)):
            num_of_factors1 *= (prime_factors1[j][1] + 1)
        num_of_factors2 = 1
        for j in xrange(len(prime_factors2)):
            num_of_factors2 *= (prime_factors2[j][1] + 1)
        if num_of_factors1 * num_of_factors2 > 500:
            print "Answer:", i * (i + 1) / 2
            break
        i += 1

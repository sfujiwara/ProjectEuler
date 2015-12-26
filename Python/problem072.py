# -*- coding: utf-8 -*-

'''
ファレイ数列の長さを求める問題.
Problem 73 のように再帰でやると計算量が大変なことになるので,
オイラーのトーシェント関数の和を求める.
'''

# -*- coding: utf-8 -*-

# Prime Factor Decomposition
# 出力は Ruby の prime_division と同じ
# x^a * y^b * z^c -> [[x, a], [y, b], [z, c]]
def pfd(n):
    prime_factors = []
    upper_threshold = n**0.5
    # 後のループを奇数だけで回すために, 2 だけ場合分けする
    if n % 2 == 0:
        factor = 2
        count = 0
        while n % factor == 0:
            n = n / factor
            count += 1
        prime_factors.append([factor, count])
    # 3 以上のの素因数を探す
    factor = 3
    while n > 1:
        # √n を超える素数は調べる必要がない
        if factor > upper_threshold:
            prime_factors.append([n, 1])
            break
        # 割り続けて素因数 factor を取り除く
        if n % factor == 0:
            count = 0
            while n % factor == 0:
                n = n / factor
                count += 1
            prime_factors.append([factor, count])
        # 3 以上の素数は全て奇数なので, 奇数だけ調べれば十分
        # 本当は素数だけを調べれば十分
        factor += 2
    return prime_factors

def totient(n):
    res_pfd = pfd(n)
    res = n
    for i in res_pfd:
        res *= (1. - 1./i[0])
    return res
    
if __name__ == '__main__':
    ans = 0
    for i in range(2, 1000001):
        ans += totient(i)
    print 'Answer:', int(ans)

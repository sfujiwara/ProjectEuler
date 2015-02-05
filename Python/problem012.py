# -*- coding: utf-8 -*-

# Prime Factor Decomposition
# 出力は Ruby の prime_division と同じ
# x^a * y^b * z^c -> [[x, a], [y, b], [z, c]]
# 正解者用のドキュメントを参考にかなり高速化したので桁がいくつか増えても大丈夫
def pfd(n):
    prime_factors = []
    max_factor = n**0.5
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
        if factor > max_factor:
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

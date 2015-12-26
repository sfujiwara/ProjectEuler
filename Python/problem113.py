# -*- coding: utf-8 -*-

'''
{1, ..., 9} から n 個選ぶ重複組合せと増加数が一対一に対応.
減少数の場合は 0 も含むが, 全部 0 のパターンは除く.
'''

from scipy.misc import comb

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)

def nPm(n, m):
    return fact(n) / fact(n-m)

def nCm(n, m):
    return nPm(n, m) / fact(m)

def nHm(n, m):
    return nCm(n+m-1, m)

## n 桁以下の増加数の個数を返す関数
def num_increasing(n):
    return sum(nHm(9, i) for i in range(1,n+1))

def num_decreasing(n):
    return sum(nHm(10, i) for i in range(1,n+1)) - n

def num_increasing2(n):
    return nCm(n + 9, 9) - 1

if __name__ == '__main__':
    n = 100
    ## ゾロ目の数は増加数と減少数の両方でカウントされているので, その分を引く
    print num_increasing(n) + num_decreasing(n) - 9 * n

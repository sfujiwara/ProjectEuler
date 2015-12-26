# -*- coding: utf-8 -*-

'''
メモ化再帰で解く.
Problem 114~117 は全部ほぼ同じ.
'''

memo = [-1] * 100

def ways(n):
    if n < 0: return 0
    if n < 2: return 1
    if memo[n] < 0:
        res = 0
        ## 長さ 1 の黒ブロックを置く
        res += ways(n-1)
        for i in [2, 3, 4]:
            ## 長さ i の色ブロックを置いた後, 長さ 1 の黒ブロックを置く
            res += ways(n-i)
        memo[n] = res
    return memo[n]

if __name__ == '__main__':
    print 'Answer:', ways(50)

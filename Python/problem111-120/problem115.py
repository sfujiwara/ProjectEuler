# -*- coding: utf-8 -*-

'''
メモ化再帰で解く.
Problem 114 と同じ.
'''

memo = [-1] * 1000000

def ways(n):
    if n < 3: return 1
    if memo[n] < 0:
        res = 0
        ## 長さ 1 の黒ブロックを置く
        res += ways(n-1)
        for i in range(50, n+1):
            ## 長さ i の赤ブロックを置いた後, 長さ 1 の黒ブロックを置く
            res += ways(n-i-1)
        memo[n] = res
    return memo[n]

if __name__ == '__main__':
    for i in range(50, 1000):
        if ways(i) > 1000000:
            print 'Answer:', i
            break

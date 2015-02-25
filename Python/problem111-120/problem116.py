# -*- coding: utf-8 -*-

'''
メモ化再帰で解く.
Problem 114 と同じ.
'''

memo_size = 1000
memo = [-1] * memo_size

def ways(n, l):
    if n < l: return 1
    if memo[n] < 0:
        res = 0
        ## 長さ 1 の黒ブロックを置く
        res += ways(n-1, l)
        ## 長さ l の色ブロックを置く
        res += ways(n-l, l)
        memo[n] = res
    return memo[n]

## l を変えながら ways を複数回走らせる場合, memo を初期化する必要がある
def reset_memo():
    global memo
    memo = [-1] * memo_size

if __name__ == '__main__':
    ans = 0
    for l in [2, 3, 4]:
        reset_memo()
        ans += (ways(50, l) - 1)
    print 'Answer:', ans

# -*- coding: utf-8 -*-

'''
コラッツ予想に関する問題.
メモ化再帰で解く.
一応メモ化しなくても何とかなるレベル.
'''

size = 1000000
memo = [0] * lim
memo[1] = 1

## コラッツ数列の長さを返す関数
def len_collatz(n):
    ## nがメモを保存する範囲を超えている場合
    if n >= size:
        if n % 2 == 0: return 1 + len_collatz(n/2)
        else: return 1 + len_collatz(3*n+1)
    ## nがメモを保持する範囲内の場合
    elif not memo[n] == 0: return memo[n]
    elif n % 2 == 0:
        memo[n] = 1+len_collatz(n/2)
        return memo[n]
    else:
        memo[n] = 1 + len_collatz(3*n + 1)
        return memo[n]

if __name__ == '__main__':
    max_length = 0
    for i in xrange(500000, 1000000):
        l = len_collatz(i)
        if l > max_length:
            max_length = l
            ans = i

    print "Answer:", ans

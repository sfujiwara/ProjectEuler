# -*- coding: utf-8 -*-

'''
色々と微妙.
リスト内包表記を使わずに書き直した方が良さそう.
'''

from itertools import count

MEMO_SIZE = 10000000
memo = [-1] * MEMO_SIZE

def partition(n):
    if n < 0: return 0
    if n == 0: return 1
    if n < MEMO_SIZE:
        if memo[n] > 0:
            return memo[n]
    ## partition() の引数が負になる範囲まで回す必要がある
    ## とりあえず [-200, 200] の範囲にした
    ## リスト内包表記では無理があるかも
    res = sum(int((-1)**(i-1)) * partition(n - (3*i**2 + i) / 2) for i in range(-200, 0) + range(1, 200))
    if n < MEMO_SIZE:
        if memo[n] < 0:
            memo[n] = res
    return res


if __name__ == '__main__':
    ## どの範囲まで調べるかを決めておけば, 上のコメントで書かれている
    ## リスト内包表記で回す範囲を大体決めることができる
    for i in range(60000):
        if partition(i) % 1000000 ==0:
            print 'Answer:', i
            break

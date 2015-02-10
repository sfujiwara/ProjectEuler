# -*- coding: utf-8 -*-


## 支払い額と硬貨のリストから, 支払い方法の組合せを数える関数
def ways(n, coin_list):
    ## リストの長さが 1 になったら, 支払い方法が存在するか判定
    if len(coin_list) == 1:
        if n % coin_list[0] == 0: return 1
        else: return 0
    res = 0
    while n >= 0:
        ## リストの末尾を削除して再帰呼び出し
        res += ways(n, coin_list[:-1])
        n -= coin_list[-1]
    return res


if __name__ == '__main__':
    coin_list = [1, 2, 5, 10, 20, 50, 100, 200]
    print 'Answer:', ways(200, coin_list)

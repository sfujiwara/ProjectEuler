# -*- coding: utf-8 -*-

import itertools

if __name__ == '__main__':
    dice_peter = (1, 2, 3, 4)
    dice_colin = (1, 2, 3, 4, 5, 6)

    ## Peter のサイコロの目のパターンを直積で全て列挙
    prod_peter = itertools.product(dice_peter, repeat=9)
    ## 各パターンで出目の和を計算
    sum_peter = [sum(i) for i in prod_peter]
    ## 出目の和が 1~36 になる回数をそれぞれカウント
    ways_peter = [sum_peter.count(i) for i in range(1, 37)]
    
    ## Colin の場合も同様
    prod_colin = itertools.product(dice_colin, repeat=6)
    sum_colin = [sum(i) for i in prod_colin]
    ways_colin = [sum_colin.count(i) for i in range(1, 37)]
    
    ans = 0
    for i in range(36):
        ans += ways_colin[i] * sum(ways_peter[(i+1):])

    print 'Answer:', round(float(ans) / (4**9 * 6**6), 7)

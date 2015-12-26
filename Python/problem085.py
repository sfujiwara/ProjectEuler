# -*- coding: utf-8 -*-

'''
とりあえす 1 <= row <= 2000, row <= col <= 2000 としている.
count_rectangular(1, 2000) >= 2000000 なので, この範囲には答えがある.
ループの範囲を真面目に絞っていないので, 8 分くらい掛かってしまう.
実は最初に 1 <= row <= 2000, 1 <= col <= 100 で試したら
あっさり答えが出てしまった.
'''

## row * col グリッドに含まれる長方形を数える関数
def count_rectangular(row, col):
    count = 0
    for i in range(1, row+1):
        for j in range(1, col+1):
            count += (row - i + 1) * (col - j + 1)
    return count

## リスト内包表記だと可読性が酷い気がする
## def count_rectangular(row, col):
##     return sum(sum((row-i+1) * (col-j+1) for j in range(1, col+1)) for i in range(1, row+1))

if __name__ == '__main__':
    ans = 0
    ## 差の最小値 (最初は適当に大きい値にしておく)
    min_diff = 10000000

    ## 1 * 2000 のグリッドで 200 万個を超えることを確認済み
    ## 本当はもう少し真面目に範囲を絞った方が良い
    for i in range(1, 2000):
        ## ここはどうやって範囲を絞るのが良いか後で考える
        for j in range(i, 2000):
            num_rect = count_rectangular(i, j)
            if abs(num_rect - 2000000) < min_diff:
                ans = i * j
                min_diff = abs(num_rect - 2000000)
            if num_rect > 2000000:
                break
    print 'Answer:', ans

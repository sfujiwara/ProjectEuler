# -*- coding: utf-8 -*-
'''
a = 直前の連続欠席数,
l = 遅刻数,
d = 残り日数,
とすると漸化式を作ることができる.
(a,l) = (0,0), (0,1), (1,0), (1,1), (2,0), (2,1)
の順番に並べた行列を作ってなんやかんややる.
'''

def ways(n):
    ## 日数と添字を合わせるために, 1 つ多めに作った
    mat = [[-1,-1,-1,-1,-1,-1] for i in range(n+1)]
    ## 日数 1 の場合のパターン数
    mat[0] = [1, 1, 1, 1, 1, 1]
    for d in range(1, n+1):
        mat[d][0] = mat[d-1][0] + mat[d-1][1] + mat[d-1][2]
        mat[d][1] = mat[d-1][1] + mat[d-1][3]
        mat[d][2] = mat[d-1][0] + mat[d-1][1] + mat[d-1][4]
        mat[d][3] = mat[d-1][1] + mat[d-1][5]
        mat[d][4] = mat[d-1][0] + mat[d-1][1]
        mat[d][5] = mat[d-1][1]
    return mat

## メモ化していない再帰なので遅い
## def way_rec(a, l, d):
##     if a == 3 or l == 2:
##         return 0
##     elif d == 0:
##         return 1
##     return ways(a+1, l, d-1) + ways(0, l+1, d-1) + ways(0, l, d-1)

if __name__ == '__main__':
    ## print 'Answer:', ways(0, 0, 30)
    mat = ways2(30)
    print 'Answer:', mat[30][0]

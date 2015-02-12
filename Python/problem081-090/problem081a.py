# -*- coding: utf-8 -*-

'''
メモ化再帰で解く.
'''

import csv

memo = [[-1] * 80 for i in range(80)]

def min_cost(row, col, mat):
    ## メモが埋まっている場合はその値を返せば良い
    if memo[row][col] > 0:
        pass
    ## スタート地点の左上はそのまま
    elif row == col == 0:
        memo[row][col] = mat[row][col]
    ## 一番上の行は左のマスから来るしかない
    elif row == 0:
        memo[row][col] = min_cost(row, col-1, mat) + mat[row][col]
    ## 一番左の列は上のマスから来るしかない
    elif col == 0:
        memo[row][col] = min_cost(row-1, col, mat) + mat[row][col]
    ## その他の場合は上のマスと左のマスのどちらかお得な方から来る
    else:
        memo[row][col] = min(min_cost(row, col-1, mat),
                             min_cost(row-1, col, mat)) + mat[row][col]
    return memo[row][col]

if __name__ == '__main__':
    mat = [[int(j) for j in i] for i in csv.reader(open('matrix.txt'))]
    print 'Answer:', min_cost(79, 79, mat)


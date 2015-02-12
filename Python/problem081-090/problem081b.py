# -*- coding: utf-8 -*-

'''
動的計画法で解く.
やっていることは本質的にメモ化再帰と同じ.
'''

import csv

if __name__ == '__main__':
    mat = [[int(j) for j in i] for i in csv.reader(open('matrix.txt'))]
    route = [[0] * 80 for i in range(80)]
    ## 面倒なので mat に上書きしてしまったが, 本当はあまり良くないかも
    for row in xrange(80):
        for col in xrange(80):
            if row == 0 and col == 0:
                pass
            elif row == 0:
                mat[row][col] = mat[row][col-1] + mat[row][col]
            elif col == 0:
                mat[row][col] = mat[row-1][col] + mat[row][col]
            else:
                mat[row][col] = min(mat[row-1][col], mat[row][col-1]) + mat[row][col]
    print 'Answer:', mat[-1][-1]

# -*- coding: utf-8 -*-

'''
大体 problem 82 と同じ.
場合分けもうちょい何とかなるだろとは思う.
オセロで言う, 各隅と各辺とその他で分けてる.
'''

import csv

INF = 10**10

if __name__ == '__main__':
    mat = [[int(j) for j in i] for i in csv.reader(open('matrix.txt'))]
    min_cost = [[INF for i in range(80)] for j in range(80)]
    for i in range(80*80):
        for row in range(80):
            for col in range(80):
                if col == 0 and row == 0:
                    min_cost[row][col] = mat[row][col]
                elif col ==0 and row == 79:
                    min_cost[row][col] = min(min_cost[row][col],
                                             min_cost[row-1][col] + mat[row][col],
                                             min_cost[row][col+1] + mat[row][col])
                elif col == 79 and row == 79:
                    min_cost[row][col] = min(min_cost[row][col],
                                             min_cost[row-1][col] + mat[row][col],
                                             min_cost[row][col-1] + mat[row][col])
                elif col ==79 and row == 0:
                    min_cost[row][col] = min(min_cost[row][col],
                                             min_cost[row+1][col] + mat[row][col],
                                             min_cost[row][col-1] + mat[row][col])
                elif row == 0:
                    min_cost[row][col] = min(min_cost[row][col],
                                             min_cost[row+1][col] + mat[row][col],
                                             min_cost[row][col+1] + mat[row][col],
                                             min_cost[row][col-1] + mat[row][col])
                elif row == 79:
                    min_cost[row][col] = min(min_cost[row][col],
                                             min_cost[row-1][col] + mat[row][col],
                                             min_cost[row][col+1] + mat[row][col],
                                             min_cost[row][col-1] + mat[row][col])
                elif col == 0:
                    min_cost[row][col] = min(min_cost[row][col],
                                             min_cost[row+1][col] + mat[row][col],
                                             min_cost[row-1][col] + mat[row][col],
                                             min_cost[row][col+1] + mat[row][col])
                elif col == 79:
                    min_cost[row][col] = min(min_cost[row][col],
                                             min_cost[row+1][col] + mat[row][col],
                                             min_cost[row-1][col] + mat[row][col],
                                             min_cost[row][col-1] + mat[row][col])
                else:
                    min_cost[row][col] = min(min_cost[row][col],
                                             min_cost[row+1][col] + mat[row][col],
                                             min_cost[row-1][col] + mat[row][col],
                                             min_cost[row][col+1] + mat[row][col],
                                             min_cost[row][col-1] + mat[row][col])
    print 'Answer:', min_cost[-1][-1]

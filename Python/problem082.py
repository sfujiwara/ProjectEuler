# -*- coding: utf-8 -*-

'''
各マスを頂点だと思って Bellman-Ford 法.
本当は更新がなくなったらループを抜けだして良いけれど, 書くのが面倒になった.
高々 |V|-1 回反復すれば終わることが保証されているので, とりあえずそれで.
'''

import csv

INF = 10**10

if __name__ == '__main__':
    mat = [[int(j) for j in i] for i in csv.reader(open('matrix.txt'))]
    min_cost = [[INF for i in range(80)] for j in range(80)]
    for i in range(80*80):
        ## update = False
        for row in range(80):
            for col in range(80):
                if col == 0:
                    min_cost[row][col] = mat[row][col]
                elif row == 0:
                    min_cost[row][col] = min(min_cost[row][col],
                                             min_cost[row+1][col] + mat[row][col],
                                             min_cost[row][col-1] + mat[row][col])
                elif row == 79:
                    min_cost[row][col] = min(min_cost[row][col],
                                             min_cost[row-1][col] + mat[row][col],
                                             min_cost[row][col-1] + mat[row][col])
                else:
                    min_cost[row][col] = min(min_cost[row][col],
                                             min_cost[row+1][col] + mat[row][col],
                                             min_cost[row-1][col] + mat[row][col],
                                             min_cost[row][col-1] + mat[row][col])
    print 'Answer:', min(i[-1] for i in min_cost)


    ## 隣接行列の作成
    ## adjacency_mat = [[INF for i in range(80*80)] for j in range(80*80)]
    ## for row in range(80):
    ##     for col in range(80):
    ##         node_id = row * 10 + col
    ##         if col >= 1:
    ##             adjacency_mat[node_id-1][node_id] = mat[row][col]
    ##         if row >= 1:
    ##             adjacency_mat[node_id-80][node_id] = mat[row][col]
    ##         if row < 79:
    ##             adjacency_mat[node_id+80][node_id] = mat[row][col]

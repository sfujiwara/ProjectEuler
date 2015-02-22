# -*- coding: utf-8 -*-

'''
メモ化再帰で解く.
計算量は O(mn).
'''

memo = [[0 for j in range(n+1)] for i in range(m+1)]

def count_routes(m, n):
    if n==0 or m==0:
        return 1
    elif memo[m][n] != 0:
        return memo[m][n]
    else:
        memo[m][n] = count_routes(m-1, n)+count_routes(m, n-1)
        ## 対称性からここのメモも埋まる
        if m < len(memo[0]) and n < len(memo):
            memo[n][m] = memo[m][n]
        return memo[m][n]

if __name__ == '__main__':
    print 'Answer:', count_routes(20, 20)

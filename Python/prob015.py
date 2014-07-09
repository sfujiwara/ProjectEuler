# -*- coding: utf-8 -*-
m, n = 20, 20
# キャッシュ
route_list = [[0 for j in range(n+1)] for i in range(m+1)]

def check_route(m, n):
    if n==0 or m==0: return 1
    elif route_list[m][n] != 0: return route_list[m][n]
    else:
        route_list[m][n] = check_route(m-1, n)+check_route(m, n-1)
        # 対称性からここのキャッシュも埋まる
        if m < len(route_list[0]) and n < len(route_list):
            route_list[n][m] = route_list[m][n]
        return route_list[m][n]

print "Answer =", check_route(m, n)

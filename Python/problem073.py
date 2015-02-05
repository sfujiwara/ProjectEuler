# -*- coding: utf-8 -*-

import sys

# 再帰呼出しの回数が多いので, 限界数を増やして強引なドリブルで突破.
sys.setrecursionlimit(10000)


# ファレイ数列 F_n で, a/b と c/d の間にある要素数を数える.
# ただし, a/b と c/d は, あるファレイ数列で隣接している必要がある.
def len_farey(a, b, c, d, n):
    if b + d > n:
        return 0
    return len_farey(a, b, a+c, b+d, n) + len_farey(a+c, b+d, c, d, n) + 1

if __name__ == '__main__':
    print 'Answer:', len_farey(1, 3, 1, 2, 12000)

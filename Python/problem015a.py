# -*- coding: utf-8 -*-

'''
→と↓を 20 個ずつ並べる組合せの問題として解く.
計算量は O(n).
Python には R の choose() のように組合せを求める関数が無い.
SciPy にはあるので, 覚えておく.
'''

from scipy.misc import comb

if __name__ == '__main__':
    ## exact = True としなかった場合, float 型で数値誤差が出る
    print 'Answer:', comb(40, 20, exact=True)

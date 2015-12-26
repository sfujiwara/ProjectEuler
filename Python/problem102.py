# -*- coding: utf-8 -*-

import numpy as np

if __name__ == '__main__':
    triangles = np.loadtxt('p102_triangles.txt', delimiter=',')
    ans = 0
    for i in triangles:
        x1, x2, x3 = i[0:2], i[2:4], i[4:6]
        ## 外積の方向が全て揃っているかどうかで判定
        dir1 = np.sign(np.cross(x1-x2, x1))
        dir2 = np.sign(np.cross(x2-x3, x2))
        dir3 = np.sign(np.cross(x3-x1, x3))
        ans += dir1 == dir2 == dir3
    print 'Answer:', ans

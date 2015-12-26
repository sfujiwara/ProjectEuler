# -*- coding: utf-8 -*-

'''
ペル方程式の最小解を得る関数はほぼ写経.
後で復習しておく.
'''

import math

def min_pell_eq(d):
    u = int(math.sqrt(d))
    p0, q0 = 1, 0
    p1, q1 = u, 1
    s, t, a = 0, 1, u
    for i in range(1000):
        s = a*t-s
        t = (d-s*s)/t
        a = (s+u) / t
        p2 = a * p1 + p0
        q2 = a * q1 + q0
        p0 = p1
        q0 = q1
        p1 = p2
        q1 = q2
        if t == 1: break
    return p0, q0, p0**2 - d * q0**2

if __name__ == '__main__':
    x_max = 0
    for i in range(1, 1001):
        if int(math.sqrt(i))**2 == i:
            pass
        else:
            x, y, a = min_pell_eq(i)
            if a == -1:
                x, y = x**2 + i * y**2, 2 * x * y
                if x_max < x:
                    print x, y, a, i, x**2 - i * y**2
                    x_max = x
                    ans = i

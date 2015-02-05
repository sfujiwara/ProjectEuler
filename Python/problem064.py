# -*- coding: utf-8 -*-

import math

# (√n - b) / a -> 1 / {c + (√n - e) / d} のように分解する, あるいは
# a / (√n - b) -> c + 1 / [1 / {d / (√n - e)}] と分解していると見ても良い
# d は必ず整数になると思われるが, 証明できていない
def frac_decomp(n, a, b):
    c = int(math.floor(a / (math.sqrt(n) - b)))
    d = (n - b**2) / a
    e = -(b - c*d)
    return [c, d, e]

# √n を連分数分解
def cont_frac_decomp(n):
    a0 = a = 1
    b0 = b = int(math.floor(math.sqrt(n)))
    c0 = b0
    c_seq = []
    if b0**2 == n: return [c0, c_seq]
    while True:
        [c, d, e] = frac_decomp(n, a, b)
        a, b = d, e
        c_seq.append(c)
        if [a0, b0] == [a, b]: break
    return [c0, c_seq]

if __name__ == '__main__':
    ans = 0
    for i in range(10001):
        tmp = cont_frac_decomp(i)
        ## print i+1, tmp
        if len(tmp[1]) % 2 == 1: ans += 1
    print 'Answer:', ans

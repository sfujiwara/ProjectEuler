# -*- coding: utf-8 -*-
# Prime Factor Decomposition
def pfd(n):
    prime_factors = []
    i = 2
    # ここを素数だけで回せばもっと速くなる
    while True:
        if n == 1: break
        # 割り続けて素因数iを取り除く
        if n%i == 0:
            count = 0
            while n%i ==0:
                n = n/i
                count += 1
            prime_factors.append([i, count])
        i += 1
    return prime_factors

print pfd(600851475143)

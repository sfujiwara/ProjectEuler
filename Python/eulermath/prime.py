# -*- coding: utf-8 -*-

import numpy as np
# import math


# def sieve(n):
#     # 0-nが素数か否かのフラグ
#     is_prime = [True]*(n+1)
#     # 0, 1 は素数ではない
#     is_prime[0], is_prime[1] = False, False
#     for i in xrange(2, int(math.sqrt(n))+1):
#         if is_prime[i]:
#             for j in xrange(i*2, n+1, i):
#                 is_prime[j] = False
#     return [i for i in xrange(n+1) if is_prime[i]]


def sieve(n):
    is_prime = np.ones(n+1, dtype=bool)
    is_prime[0], is_prime[1] = False, False
    for i in xrange(2, int(np.sqrt(n)+1)):
        if is_prime[i]:
            is_prime[np.arange(i*2, n+1, i)] = False
    return np.where(is_prime)[0]

# -*- coding: utf-8 -*-
import math

# 素数リストpnと自然数nを与えると素数か判定する関数
def is_prime(n, plist):
    for i in plist:
        if n%i == 0: return False
        elif i > math.sqrt(n): return True
    return True

prime_list = [2]
i = 3
while(True):
    if is_prime(i, prime_list): prime_list.append(i)
    if len(prime_list)==10001: break
    i += 1
print "Answer =", prime_list[-1]

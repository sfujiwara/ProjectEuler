import math
from datetime import datetime

# n以下の素数列を返す関数(エラトステネスの篩)
def get_prime(n):
    prime = [True]*(n+1)
    prime[0], prime[1] = False, False
    for i in xrange(2, int(math.sqrt(n))+1):
        if prime[i]:
            for j in xrange(i*2, n+1, i):
                prime[j] = False
    p = []
    for i in xrange(n+1):
        if prime[i]: p.append(i)
    return p

# 巡回素数か調べる関数(is cyclic primal number)
def is_cpn(n, pl):
    tmp = n
    digit = len(str(n))
    for i in xrange(digit):
        tmp = tmp*10 + tmp/10**(digit-1) - tmp/10**(digit-1)*10**(digit)
        if tmp not in pl: return False
    return True

ans = 0
prime_list = get_prime(1000000)
for i in prime_list:
    if is_cpn(i, prime_list):
        ans += 1
        print ans, "個目の巡回素数:", i
print "Answer =", ans

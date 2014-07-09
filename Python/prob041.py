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

def is_npandigital(n):
    pandigit = [[1],[1,2],[1,2,3],[1,2,3,4],[1,2,3,4,5],[1,2,3,4,5,6],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8,9]]
    string = str(n)
    digit = len(string)
    num_list = []
    for i in xrange(digit):
        num_list.append(int(string[i]))

    if set(pandigit[digit-1]) == set(num_list): return True
    else: return False

# 9桁のpandigital数は3の倍数なので調べなくて良い
prime = get_prime(99999999)
for i in reversed(prime):
    if is_npandigital(i): print i

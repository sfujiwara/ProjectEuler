import math

# エラトステネスの篩でn以下の素数列を返す関数
def sieve(n):
    # 0-nが素数か否かのフラグ
    flag = [True]*(n+1)

    # とりあえず0, 1は素数ではない
    flag[0], flag[1] = False, False

    for i in xrange(2, int(math.sqrt(n))+1):
        if flag[i]:
            for j in xrange(i*2, n+1, i): flag[j] = False
    return [i for i in xrange(n+1) if flag[i]]

# 2乗して2倍したヤツら
squares2 = [2*pow(i,2) for i in xrange(1000)]

# 素数を適当に沢山
primes = sieve(10000)

for i in xrange(3, 10000, 2):
    flag = True
    for j in primes:
        #if j > i: break
        if i-j in squares2: flag = False
    if flag: print i

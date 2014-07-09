import random

def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

def is_prime3(q,k=50):
    q = abs(q)
    #計算するまでもなく判定できるものははじく
    if q == 2: return True
    if q < 2 or q&1 == 0: return False

    #n-1=2^s*dとし（但しaは整数、dは奇数)、dを求める
    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1
    
    #判定をk回繰り返す
    for i in xrange(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        #[0,s-1]の範囲すべてをチェック
        while t != q-1 and y != 1 and y != q-1: 
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True

def get_length(a, b):
    i = 0
    while(True):
        if is_prime(i**2 + a*i + b) == False: return i
        i = i+1


prime = []
for i in xrange(1, 1000):
    if is_prime(i): prime.append(i)

maxl = 0
for i in xrange(-999, 1000):
    a = i
    for j in prime:
        b = j
        tmp = get_length(a, b)
        if tmp > maxl:
            maxl = tmp
            ans = a*b

print ans


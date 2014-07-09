cache = [[0 for i in xrange(101)] for j in xrange(101)]

def P(n, m):
    if not cache[n][m] == 0: return cache[n][m]
    elif m > n: return 0
    elif m==1 or n==m: return 1
    else:
        cache[n][m] = P(n-m, m) + P(n-1, m-1)
        return cache[n][m]

print sum([P(100, i) for i in xrange(1, 100)])

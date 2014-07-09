def pentagonal(n): return [i*(3*i-1)/2 for i in range(1, n+1)]

n = 5000
p = pentagonal(n)

for i in range(n-1):
    for j in range(i+1, n):
        if ((p[i]+p[j]) in p) and ((p[j]-p[i]) in p):
            print i, j, p[j]-p[i]

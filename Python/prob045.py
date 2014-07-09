def triangle(n): return [i*(i+1)/2 for i in range(1,n+1)]
def pentagonal(n): return [i*(3*i-1)/2 for i in range(1,n+1)]
def hexagonal(n): return [i*(2*i-1) for i in range(1,n+1)]

n = 120000
t = triangle(n)
p = pentagonal(n/2)
h = hexagonal(n/3)

for i in t:
    if (i in p) and (i in h): print i

#3919257

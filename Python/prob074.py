def factorial(n):
    if n <= 1: return 1
    else: return n * factorial(n-1)

def get_next_term(n):
    num_list = [int(i) for i in str(n)]
    return sum(factorial(i) for i in num_list)

ans = 0
for i in xrange(1000000):
    terms = [i]
    while True:
        next_term = get_next_term(terms[-1])
        if next_term in terms: break
        terms.append(next_term)
    if len(terms) == 60: ans += 1

print "Answer =", ans

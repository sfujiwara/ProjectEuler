# n‚Ì^‚Ì–ñ”‚Ì˜a‚ğ•Ô‚·ŠÖ”
def d(n):
    divisor_sum = 0
    for i in xrange(1, n):
        if n%i == 0: divisor_sum += i
    return divisor_sum

sum = 0
for i in xrange(1, 10000):
    if i == d(d(i)) and i!= d(i):
        # print i
        sum += i

print sum

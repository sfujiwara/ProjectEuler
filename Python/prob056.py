def sum_digits(n):
    dsum = 0
    string = str(n)
    for i in xrange(len(string)):
        dsum += int(string[i])
    return dsum

ans = 0
for i in xrange(1,100):
    for j in xrange(1, 100):
        tmp = sum_digits(i**j)
        if tmp > ans: ans = tmp

print "Answer =", ans

# a: •ªŽq, b: •ª•ê
a, b = [1], [1]
ans = 0

for i in xrange(1001):
    a.append(a[i] + 2*b[i])
    b.append(a[i] + b[i])
    if len(str(a[i])) > len(str(b[i])): ans += 1

print "Answer =", ans

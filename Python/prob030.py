num = []

ans = 0
for i in xrange(2, 354294):
    num = str(i)
    tmp = 0
    for j in xrange(len(num)):
        tmp += int(num[j])**5
    if tmp == i:
        print i
        ans += i
print "ans = ", ans

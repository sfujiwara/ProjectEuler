f1, f2, ans = 1, 1, 0

while f2 < 4000000:
    if f2 % 2 == 0:
        ans += f2
    f1, f2 = f2, f1 + f2

print 'Answer:', ans

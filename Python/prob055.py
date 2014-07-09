def reverse_sum(n): return n + int(str(n)[::-1])

# ‰ñ•¶”‚©’²‚×‚éŠÖ”
def is_palindrome(n): return str(n) == str(n)[::-1]

ans = 0
for i in xrange(10000):
    n = i
    flag = True
    count = 0
    while count <= 50:
        n = reverse_sum(n)
        if is_palindrome(n):
            flag = False
            break
        count += 1
    if flag:
        ans += 1

print "Answer =", ans

# x‚ª‰ñ•¶”‚©’²‚×‚éŠÖ”
def check_palindrome(x): return str(x) == str(x)[::-1]

ans = 0
for i in xrange(1000000):
    if check_palindrome(i) and check_palindrome(format(i, 'b')):
        ans += i
print ans

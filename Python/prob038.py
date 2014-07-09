# Pandigital”‚©’²‚×‚éŠÖ”
def is_pandigital(n):
    num = []
    pandigit = set([1,2,3,4,5,6,7,8,9])
    string = str(n)
    if len(string) != 9: return False
    for i in xrange(9): num.append(int(string[i]))
    if set(num) == pandigit: return True
    else: return False

for i in xrange(1, 10000):
    for j in xrange(2, 7):
        product = ""
        for k in xrange(1, j):
            product += str(i*k)
        if is_pandigital(int(product)):
            print product


# -*- coding: utf-8 -*-

def is_pandigital(n):
    return set(str(n)) == set('123456789')

if __name__ == '__main__':
    for i in xrange(1, 10000):
        for j in xrange(2, 7):
            product = ""
            for k in xrange(1, j):
                product += str(i*k)
            if len(product) ==9 and is_pandigital(int(product)):
                ans = product
    print 'Answer:', ans

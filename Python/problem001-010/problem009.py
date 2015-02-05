# -*- coding: utf-8 -*-


## {a, b, c} がピタゴラス数か判定する関数.
## ただし, a < b < c とする.
def is_pythagorean_triplet(a, b, c):
    return a**2 + b**2 == c**2

if __name__ == '__main__':
    ## a を回すループ (a は最大でも 332)
    for i in xrange(1, 332):
        ## b を回すループ (b は最大でも 499)
        for j in xrange(i, 499):
            a, b, c = i, j, 1000 - (i + j)
            if is_pythagorean_triplet(a, b, c):
                print '{a, b, c} =', [a, b, c]
                print 'Answer:', a * b * c

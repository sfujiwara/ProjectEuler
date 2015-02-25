# -*- coding: utf-8 -*-

def is_increasing(n):
    n_list = [int(i) for i in str(n)]
    return n_list == sorted(n_list)

def is_decreasing(n):
    n_list = [int(i) for i in str(n)]
    return n_list == sorted(n_list, reverse=True)

if __name__ == '__main__':
    count = 0.
    i = 11
    while True:
        ## if i % 100000 == 0: print i
        if not is_increasing(i):
            if not is_decreasing(i):
                count += 1
        if count / i >= 0.99:
            ans = i
            break
        i += 1
    print 'Answer:', ans

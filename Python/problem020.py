# -*- coding: utf-8 -*-

def fact(x):
    if x <= 1:
        return 1
    else:
        return x * fact(x-1)

if __name__ == '__main__':
    print 'Answer:', sum(int(x) for x in str(fact(100)))

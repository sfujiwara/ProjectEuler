# -*- coding: utf-8 -*-

'''
1~2時間くらい掛かるウンコード.
'''

def is_reversible(n):
    if n % 10 == 0:
        return False
    res = True
    for i in set(str(n + int(str(n)[::-1]))):
        if int(i) % 2 == 0:
            res = False
            break
    return res

if __name__ == '__main__':
    ans = 0
    for i in xrange(10**9):
        ans += is_reversible(i)
    print 'Answer:', ans

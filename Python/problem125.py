# -*- coding: utf-8 -*-

'''
squared_sum(m, n) は (m1, n1), (m2, n2) のように異なる範囲を指定しても,
同じ数になることがあるので注意.
'''

## m~n までの二乗和を返す関数
def squared_sum(m, n):
    return (n*(n+1)*(2*n+1) - (m-1)*m*(2*m-1)) / 6

def is_palindromic(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    ans = []
    for m in range(1, 10000):
        for n in range(m+1, 10000):
            num = squared_sum(m, n)
            if num >= 10**8:
                break
            if is_palindromic(num):
                ans.append(num)
    print 'Answer:', sum(set(ans))

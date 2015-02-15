# -*- coding: utf-8 -*-

'''
ファレイ数列の問題.
'''

if __name__ == '__main__':
    a, b = 2, 5
    while b + 7 <= 1000000:
        a, b = a + 3, b + 7 
    print 'Answer:', a

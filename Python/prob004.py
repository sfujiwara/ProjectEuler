# -*- coding: utf-8 -*-
# nが回文数か調べる関数
def is_palindrome(n): return str(n) == str(n)[::-1]

palindrome_list = []

for i in xrange(100, 1000):
    for j in xrange(i, 1000):
        if(is_palindrome(i*j)): palindrome_list.append(i*j)
        
print max(palindrome_list)

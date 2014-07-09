# -*- coding: utf-8 -*-
import timeit

# 数値をリストに変換する関数その1
def num2list1(n): return [int(i) for i in str(n)]

# 数値をリストに変換する関数その2
def num2list2(n): return map(int, str(n))

def num2list3(n):
    num_list = []
    while n > 0:
        num_list.append(n%10)
        n /= 10
    return num_list

n = 2**1000

ans1 = num2list1(n)
ans1 = num2list2(n)
ans1 = num2list3(n)

print "Answer =", sum(num2list2(n))
print "Answer =", sum(num2list1(n))
print "Answer =", sum(num2list3(n))

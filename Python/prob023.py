# -*- coding:utf-8 -*-
from datetime import datetime

# 自然数xが過剰数かどうか調べる関数
def check_abundance(x):
    dsum = 0
    for i in xrange(x/2, 0, -1):
        if x%i == 0: dsum += i
        if dsum > x: return True
    return False

# nが過剰数の和で表せるか
def check_sum(n, abd):
    for i in abd:
        if i > n/2: break
        if n - i in abd: return True
    return False

t0 = datetime.now()
print t0

# 1-28123の範囲で過剰数を全てリストアップ
n = 28123
abdnums = []
for i in xrange(1, n+1):
    if(check_abundance(i)): abdnums.append(i)

t1 = datetime.now()
print t1
print t1 - t0

# 過剰数の和で表せない数の合計
SUM = 0
for i in xrange(1, n+1):
    if check_sum(i, abdnums)==False: SUM += i

t2 = datetime.now()
print t2
print t2 - t1

print SUM

"""
anum = len(abundant_nums)
# 2つの過剰数の和のパターンをメモ
sum_pattern = [[0 for j in range(len(abundant_nums))] for i in range(len(abundant_nums))]
for i in xrange(anum):
    for j in xrange(anum):
        sum_pattern[i][j] = abundant_nums[i]+abundant_nums[j]

sum = 0
for i in xrange(1, 28124):
    flag = 1
    for j in xrange(len(abundant_nums)):
        for k in xrange(len(abundant_nums)):
            if sum_pattern[j][k] == i: flag = 0
    if flag: sum += i

# 1-28123の範囲で2つの過剰数の和で表せない
sum_comb = 0
for i in xrange(28124):
    flag = 0
    for j in xrange(len(abundant_nums)):
"""

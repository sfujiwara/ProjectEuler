# -*- coding: utf-8 -*-
# {a, b, c}がピタゴラス数か判定する関数
def is_pythagoras_nums(a, b, c):
    # 0や負の値が混ざっているときはFalseを返す
    if a<=0 or b<=0 or c<=0: return False
    else: return pow(a,2)+pow(b,2) == pow(c,2)

# aを回すループ
for i in range(1, 500):
    # bを回すループ
    for j in range(i, 1000):
        a, b, c = i, j, 1000-(i+j)
        if is_pythagoras_nums(a, b, c):
            print "{a, b, c}=", "{", a, b, c, "}"
            print "a*b*c =", a*b*c

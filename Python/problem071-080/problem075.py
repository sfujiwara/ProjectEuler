# -*- coding: utf-8 -*-

'''
原始ピタゴラス数を生成して, その倍数を調べる.
生成方法は wikipedia あたりを参照.
'''

import fractions

if __name__ == '__main__':
    max_l = 1500000
    count = [0] * (max_l + 1)

    for n in range(1, int(max_l**0.5)+1):
        for m in range(n+1, int(max_l**0.5)+1):
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            l = a + b + c
            if l > max_l:
                break
            ## この条件を充たせば (a, b, c) は原始ピタゴラス数
            if (m - n) % 2 == 1 and fractions.gcd(m, n) == 1:
                ## 原始ピタゴラス数の倍数を調べる
                i = 1
                while l * i <= max_l:
                    count[l*i] += 1
                    i += 1

    print 'Answer:', sum(i for i in count if i == 1)

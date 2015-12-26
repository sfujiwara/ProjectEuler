# -*- coding: utf-8 -*-


# nが回文数か調べる関数
# mod 10 で調べるより, 文字列で反転させた方がちょっと速い
def is_palindrome(n):
    return str(n) == str(n)[::-1]


def is_palindrome2(n):
    m = n
    reversed = 0
    while n > 0:
        reversed = 10 * reversed + n % 10
        n = n / 10
    return reversed == m

if __name__ == '__main__':
    ans = 0
    # 6 桁の回分数は必ず 11 の倍数になる
    for i in xrange(110, 1000, 11):
        for j in xrange(i, 1000):
            cand = i * j
            if(is_palindrome(cand) and cand > ans):
                ans = cand
    print ans

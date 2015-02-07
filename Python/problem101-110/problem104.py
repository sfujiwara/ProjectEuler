# -*- coding: utf-8 -*-

def is_pandigital(n):
    return set(str(n)) == set('123456789')


if __name__ == '__main__':
    f1, f2 = 1, 1
    k = 1
    while True:
        k += 1
        ## 下 9 桁が panditital かどうか調べる
        if is_pandigital(f2 % 10**9):
            ## 上 9 桁を調べるときは, 文字列に変換してから反転させて, 下 9 桁を調べる
            if is_pandigital(int(str(f2)[::-1]) % 10**9):
                print 'Answer:', k
                break
        f1, f2 = f2, f1 + f2

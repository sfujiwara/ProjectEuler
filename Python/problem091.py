# -*- coding: utf-8 -*-

'''
力ずくで整数格子点を全部調べただけ.
itertools を使えばもうちょい綺麗に書ける.
'''

## 原点, (x1,y1), (x2,y2) がなす三角形が直角三角形か判定する関数
def is_right_triangle(x1, y1, x2, y2):
    ## 2点が重なる場合を除く
    if (x1 == x2 and y1 == y2) \
    or (x1 == 0 and y1 == 0) \
    or (x2 == 0 and y2 == 0):
        return False
    ## 内積を3つ求めてどれか一つが0なら直角三角形
    elif x1*x2 + y1*y2 == 0 \
    or x1*(x2-x1) + y1*(y2-y1) == 0 \
    or x2*(x1-x2) + y2*(y1-y2) == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    ans = 0
    for x1 in range(51):
        for y1 in range(51):
            for x2 in range(51):
                for y2 in range(51):
                    ans += is_right_triangle(x1, y1, x2, y2)
    print 'Answer:', ans / 2

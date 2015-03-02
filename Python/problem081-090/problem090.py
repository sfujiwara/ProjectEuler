# -*- coding: utf-8 -*-

import itertools

def is_possible(d1, d2):
    ## 01 が作れるかどうか
    if not d1[0]*d2[1] + d1[1]*d2[0]:
        return False
    ## 04 が作れるかどうか
    elif not d1[0]*d2[4] + d1[4]*d2[0]:
        return False
    ## 09 が作れるかどうか
    elif not d1[0]*d2[9] + d1[9]*d2[0] + d1[0]*d2[6] + d1[6]*d2[0]:
        return False
    ## 16 が作れるかどうか
    elif not d1[1]*d2[6] + d1[6]*d2[1] + d1[1]*d2[9] + d1[9]*d2[1]:
        return False
    ## 25 が作れるかどうか
    elif not d1[2]*d2[5] + d1[5]*d2[2]:
        return False
    ## 36 が作れるかどうか
    elif not d1[3]*d2[6] + d1[6]*d2[3] + d1[3]*d2[9] + d1[9]*d2[3]:
        return False
    ## 49 が作れるかどうか
    elif not d1[4]*d2[9] + d1[9]*d2[4] + d1[4]*d2[6] + d1[6]*d2[4]:
        return False
    ## 64 が作れるかどうか
    elif not d1[6]*d2[4] + d1[4]*d2[6] + d1[9]*d2[4] + d1[4]*d2[9]:
        return False
    ## 81 が作れるかどうか
    elif not d1[8]*d2[1] + d1[1]*d2[8]:
        return False
    else:
        return True


if __name__ == '__main__':
    ans = 0
    for i in itertools.combinations(range(10), 6):
        for j in itertools.combinations(range(10), 6):
            dice1 = [False] * 10
            dice2 = [False] * 10
            for k in i:
                dice1[k] = True
            for k in j:
                dice2[k] = True
            if is_possible(dice1, dice2):
                ans += 1

    print 'Answer:', ans / 2

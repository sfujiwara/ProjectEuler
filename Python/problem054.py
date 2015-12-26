# -*- coding: utf-8 -*-

import collections

'''
Four of a Kind 以上の役は結局出てこないっぽい
がっかり
'''
score = {'High Card':0, 'One Pair':1, 'Two Pairs':2, 'Three of a Kind':3,
         'Straight':4, 'Flush':5, 'Full House':6, 'Four of a Kind':7,
         'Straight Flush':8, 'Royal Flush':9}

## 役を調べる関数
def rank(hand):
    ## nums = hand[0]
    nums = collections.Counter(hand[0]).items()
    nums.sort(key=lambda x:(x[1], x[0]), reverse=True)
    nums = zip(*nums)
    test2 = [i[0] for i in test]
    marks = hand[1]
    ## Flush かどうかの判定
    is_flush = (len(set(marks)) == 1)
    ## Straight かどうかの判定
    is_straight = max(nums[0]) - min(nums[0]) == 4 and len(nums[0]) == 5
    ## Straight かつ Flush の場合
    if is_flush and is_straight:
        if max(nums[0]) == 14:
            return ['Royal Flush', nums[0]]
        else:
            return ['Straight Flush', nums[0]]
    ## Flush だけど Straight ではない場合
    elif is_flush:
        return ['Flush', nums[0]]
    ## Straight だけど Flush ではない場合
    elif is_straight:
        return ['Straight', nums[0]]
    ## Straight でも Flush でもない場合
    else:
        if len(nums[0]) == 5:
            return ['High Card', nums[0]]
        elif len(nums[0]) == 4:
            return ['One Pair', nums[0]]
        elif len(nums[0]) == 3:
            if max(nums[1]) == 3:
                return ['Three of a Kind', nums[0]]
            else:
                return ['Two Pairs', nums[0]]
        elif len(nums[0]) == 2:
            if max(nums[1]) == 4:
                return ['Four of a Kind', nums[0]]
            else:
                return ['Full House', nums[0]]
        return 'Unknown'
            
def judge(hand_p1, hand_p2):
    rank_p1 = rank(hand_p1)
    rank_p2 = rank(hand_p2)
    if score[rank_p1[0]] == score[rank_p2[0]]:
        for i in range(len(rank_p1[1])):
            if rank_p1[1][i] > rank_p2[1][i]: return True
            if rank_p1[1][i] < rank_p2[1][i]: return False
    else: return score[rank_p1[0]] > score[rank_p2[0]]

if __name__ == '__main__':
    f = open('p054_poker.txt', 'r')
    hands = f.read()
    hands = hands.rstrip('\n')
    hands = hands.split('\n')
    dic = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
    ans = 0
    for i in hands:
        hand_p1p2 = i.split(' ')
        ## hand_p1, hand_p2 = hand_p1p2[:5], hand_p1p2[5:]
        marks = [j[1] for j in hand_p1p2]
        nums = [dic[j[0]] if j[0] in dic else int(j[0]) for j in hand_p1p2]
        hand_p1 = [nums[:5], marks[:5]]
        hand_p2 = [nums[5:], marks[5:]]
        test = collections.Counter(nums).items()
        ## print test
        test.sort(key=lambda x:(x[1], x[0]), reverse=True)
        ## print test
        print hand_p1p2
        print rank(hand_p1), rank(hand_p2), judge(hand_p1, hand_p2)
        if judge(hand_p1, hand_p2): ans += 1
    print 'Answer:', ans

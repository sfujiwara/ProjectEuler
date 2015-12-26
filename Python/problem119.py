# -*- coding: utf-8 -*-

'''
超いい加減に範囲を設定したら正しい答えが出てしまった.
酷すぎる.
'''

if __name__ == '__main__':
    ans = []
    for i in range(2, 1000):
        for j in range(2, 20):
            num = i**j
            if i == sum(int(k) for k in str(num)):
                ans.append(num)
    print 'Answer:', sorted(ans)[29]

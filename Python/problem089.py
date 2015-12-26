# -*- coding: utf-8 -*-

'''
置換の順番を変えると最適にならないことに注意する.
例えば VIIII に対して
['VIIII','IX'], ['IIII','IV'] を
['IIII','IV'], ['VIIII','IX'] と順番を変えた場合損をする.
dic の置換だけで正しい答えが出てしまったけれど,
VIV -> IX, LXL -> XC, DCD -> CM の置換も必要な気がする.
どういう順番で何回置換すれば確実に最適解が出るのかよくわからない.
'''

import re

if __name__ == '__main__':
    dic = [['IIIII','V'], ['VV','X'],
           ['XXXXX','L'], ['LL','C'],
           ['CCCCC','D'], ['DD','M'],
           ['VIIII','IX'], ['IIII','IV'], ## ここからは引き算で節約できる分
           ['LXXXX','XC'], ['XXXX','XL'],
           ['DCCCC','CM'], ['CCCC','CD'],]

    ans = 0
    for i in open('p089_roman.txt', 'r'):
        str_original = str_min = i
        ## dic の通り順番に文字列を置換していく
        for j in dic:
            str_min = re.sub(j[0], j[1], str_min)
        ans += len(str_original) - len(str_min)
    print 'Answer:', ans

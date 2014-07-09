"""
0-6を日-土までの曜日に対応させる(1901年の1月1日は火曜日なので3)
※ 1900年は閏年でないことに注意
"""

# 月の初めの曜日を保存しておく変数(day of week)
dow = 2
# 月の始めが日曜日になる回数をカウントする変数
count = 0

# 1901年から2001年を調べる
for i in xrange(1901,2001):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # 閏年を場合分け
    if i%4 == 0 and (i%100 != 0 or i%400 == 0):
        #print i, "年は閏年"
        months[1] = 29

    print i, "年で日曜から始まる月"

    # 1月から12月を調べる
    for j in xrange(12):
        #print dow
        # 月の始めが日曜だった場合countを1増やす
        if dow == 0:
            count = count+1
            print j+1, "月"

        dow = (dow+(months[j]%7))%7

print "\n合計", count, "回"

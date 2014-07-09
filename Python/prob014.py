# -*- coding: utf-8 -*-
lim = 100000000
cache = [0]*lim
cache[1] = 1

# メモ化しないと耐えられないレベルではないが遅い
def check_length(n):
    # nがキャッシュを保存する範囲を超えている場合
    if n >= lim:
        if n%2 == 0: return 1+check_length(n/2)
        else: return 1+check_length(3*n+1)
    # nがキャッシュを保持する範囲内の場合
    elif not cache[n] == 0: return cache[n]
    elif n%2 == 0:
        cache[n] = 1+check_length(n/2)
        return cache[n]
    else:
        cache[n] = 1 + check_length(3*n+1)
        return cache[n]

max_length = 0
for i in xrange(500000, 1000000):
    tmp = check_length(i)
    if tmp > max_length:
        max_length = tmp
        ans = i

print "Answer =", ans

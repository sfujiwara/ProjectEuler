# -*- coding: utf-8 -*-
f1, f2, ans = 1, 1, 0
while f1+f2 < 4000000:
    f3 = f1+f2
    if f3 % 2 == 0: ans += f3
    f1, f2 = f2, f3
print ans

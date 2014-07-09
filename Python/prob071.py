# -*- coding: utf-8 -*-
# ファレイ数列の問題
a, b = 2, 5
while True:
    if b+7 > 1000000: break
    else: a, b = a+3, b+7
    
print a, b

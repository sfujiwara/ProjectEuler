# -*- coding: utf-8 -*-

prime_list = [2, 3]
cand = 3
k = 1
n = 10001

while(True):
    ## 3 より大きい素数は 6k + 1 or 6k - 1 の形で書ける.
    ## まずは 6k - 1 が素数か調べる.
    cand = 6 * k - 1
    isprime = True
    for i in prime_list:
        ## 素数で割り切れたら, 素数ではない.
        if cand % i == 0:
            isprime = False
            break
        ## √cand 未満の素数は調べる必要がない.
        if cand < i**2:
            isprime = True
            break
    ## cand が素数ならば, 素数リストに加える.
    if isprime:
        prime_list.append(cand)
        if len(prime_list) >= n:
            break

    ## 6k + 1 についても同様に調べる.
    cand = 6 * k + 1
    isprime = True
    for i in prime_list:
        if cand % i == 0:
            isprime = False
            break
        if cand < i**2:
            isprime = True
            break
    if isprime:
        prime_list.append(cand)
        if len(prime_list) >= n:
            break

    k += 1

print "Answer:", prime_list[-1]

coin_list = [1, 2, 5, 10, 20, 50, 100, 200]

def search(x, coin):
    if x == 0: return 1
    if x < 0: return 0
    if len(coin) == 0: return 0
    comb = 0
    i = 0
    while i < (x/coin[-1]+1):
        #print coin[0:-1], comb
        comb += search(x-coin[-1]*i, coin[0:-1])
        i += 1
    return comb

print search(200, coin_list)

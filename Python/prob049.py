import math

# エラトステネスの篩でn以下の素数列を返す関数
def sieve(n):
    # 0-nが素数か否かのフラグ
    flag = [True]*(n+1)

    # とりあえず0, 1は素数ではない
    flag[0], flag[1] = False, False

    for i in xrange(2, int(math.sqrt(n))+1):
        if flag[i]:
            for j in xrange(i*2, n+1, i): flag[j] = False
    return [i for i in xrange(n+1) if flag[i]]

def are_interesting(x, y, z):
    if set([i for i in str(x)]) == set([i for i in str(y)]):
        if set([i for i in str(y)]) == set([i for i in str(z)]):
            return True
    return False

prime_list = sieve(10000)

for i in prime_list:
    if i+3330 in prime_list:
        if i+6660 in prime_list:
            if are_interesting(i, i+3330, i+6660): print i, i+3330, i+6660

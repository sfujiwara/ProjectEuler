# Prime Factor Decomposition
def pfd(n):
    prime_factors = []
    i = 2
    # ������f�������ŉ񂹂΂����Ƒ����Ȃ�
    while True:
        if n == 1: break
        # ���葱���đf����i����菜��
        if n%i == 0:
            count = 0
            while n%i ==0:
                n = n/i
                count += 1
            prime_factors.append([i, count])
        i += 1
    return prime_factors

i = 2
while True:
    prime_factors = pfd(i*(i+1)/2)
    num_of_factors = 1
    for j in xrange(len(prime_factors)):
        num_of_factors *= (prime_factors[j][1]+1)
    if num_of_factors > 500:
        print "Answer =", i*(i+1)/2
        break
    i += 1

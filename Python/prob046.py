import math

# �G���g�X�e�l�X��⿂�n�ȉ��̑f�����Ԃ��֐�
def sieve(n):
    # 0-n���f�����ۂ��̃t���O
    flag = [True]*(n+1)

    # �Ƃ肠����0, 1�͑f���ł͂Ȃ�
    flag[0], flag[1] = False, False

    for i in xrange(2, int(math.sqrt(n))+1):
        if flag[i]:
            for j in xrange(i*2, n+1, i): flag[j] = False
    return [i for i in xrange(n+1) if flag[i]]

# 2�悵��2�{�������c��
squares2 = [2*pow(i,2) for i in xrange(1000)]

# �f����K���ɑ�R
primes = sieve(10000)

for i in xrange(3, 10000, 2):
    flag = True
    for j in primes:
        #if j > i: break
        if i-j in squares2: flag = False
    if flag: print i

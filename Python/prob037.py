import math
from datetime import datetime

# n�ȉ��̑f�����Ԃ��֐�(�G���g�X�e�l�X���)
def get_prime(n):
    prime = [True]*(n+1)
    prime[0], prime[1] = False, False
    for i in xrange(2, int(math.sqrt(n))+1):
        if prime[i]:
            for j in xrange(i*2, n+1, i):
                prime[j] = False
    p = []
    for i in xrange(n+1):
        if prime[i]: p.append(i)
    return p

# �����؂�l�߂Ă��f�������ׂ�֐�
def is_interesting(n, pl):
    digit = len(str(n))
    # 1���̐���not interesting
    if digit == 1: return False
    
    tmp = n
    # �E������
    for i in xrange(1, digit):
        tmp = tmp/10
        if tmp not in pl: return False

    tmp = n
    # ��������
    for i in xrange(1, digit):
        tmp = tmp%(10**(digit-i))
        if tmp not in pl: return False

    return True

ans = 0
prime_list = get_prime(1000000)
for i in prime_list:
    if is_interesting(i, prime_list):
        ans += i
        print i, "is Interesting!!:"
print "Answer =", ans

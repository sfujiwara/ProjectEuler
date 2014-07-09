import random

# �~���[�E���r���e�X�g
def is_prime(q,k=50):
    q = abs(q)
    #�v�Z����܂ł��Ȃ�����ł�����̂͂͂���
    if q == 2: return True
    if q < 2 or q&1 == 0: return False

    #n-1=2^s*d�Ƃ��i�A��a�͐����Ad�͊)�Ad�����߂�
    d = (q-1)>>1
    while d&1 == 0:
        d >>= 1
    
    #�����k��J��Ԃ�
    for i in xrange(k):
        a = random.randint(1,q-1)
        t = d
        y = pow(a,t,q)
        #[0,s-1]�͈̔͂��ׂĂ��`�F�b�N
        while t != q-1 and y != 1 and y != q-1: 
            y = pow(y,2,q)
            t <<= 1
        if y != q-1 and t&1 == 0:
            return False
    return True

prime_count = 0.

# i�͑w�̐�
for i in xrange(1, 1000000):
    # ����
    x1 = pow(2*i, 2) + 1
    #print x1
    # �E��
    x2 = pow(2*i, 2) - (2*i-1)
    #print x2
    # ����
    x3 = pow(2*i+1, 2) - 2*i
    #print x3

    if is_prime(x1): prime_count += 1
    if is_prime(x2): prime_count += 1
    if is_prime(x3): prime_count += 1

    prime_ratio = prime_count / (i*4+1)

    if prime_ratio <= 0.1:
        print i*2+1
        break

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



prime_list = sieve(1000000)

for i in prime_list:
    num_list = [int(x) for x in str(i)]
    if num_list.count(1) == 3:
        count = 1
        for j in xrange(2, 10):
            if int(str(i).replace("1", str(j))) in prime_list: count += 1
        if count == 8: print i
            

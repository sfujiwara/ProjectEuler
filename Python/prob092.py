n = 10000000
cache_list89 = [False]*n
cache_list1 = [False]*n

def converge_to_89(n):
    # ���̍����v�Z
    next_term = sum([int(i)**2 for i in str(n)])
    
    # �������Ă���Δ��茋�ʂ�Ԃ�
    if next_term == 89: return True
    if next_term == 1: return False
    
    # �L���b�V���������X�g���`�F�b�N����
    if cache_list89[next_term]: return True
    if cache_list1[next_term]: return False
    
    # ����ȊO�̏ꍇ�͍ċA
    return converge_to_89(next_term)

count = 0
for i in xrange(1,n):
    if converge_to_89(i):
        count += 1
        cache_list89[i] = True
    else: cache_list1[i] = True
    if i%100000==0: print i

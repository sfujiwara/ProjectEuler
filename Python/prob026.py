# ���R��n�ɑ΂���1/n�̏z�߂̒�����Ԃ��֐�
def get_lor(n):
    j = 1
    reminder = []
    while(True):
        r = 10**j % n
        if r in reminder: return j-1
        reminder.append(r)
        j = j+1


ans = 0
length = 1
for i in xrange(1, 1000):
    tmp = get_lor(i)
    if tmp > length:
        length = tmp
        ans = i
    

"""
0-6���-�y�܂ł̗j���ɑΉ�������(1901�N��1��1���͉Ηj���Ȃ̂�3)
�� 1900�N�͉[�N�łȂ����Ƃɒ���
"""

# ���̏��߂̗j����ۑ����Ă����ϐ�(day of week)
dow = 2
# ���̎n�߂����j���ɂȂ�񐔂��J�E���g����ϐ�
count = 0

# 1901�N����2001�N�𒲂ׂ�
for i in xrange(1901,2001):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # �[�N���ꍇ����
    if i%4 == 0 and (i%100 != 0 or i%400 == 0):
        #print i, "�N�͉[�N"
        months[1] = 29

    print i, "�N�œ��j����n�܂錎"

    # 1������12���𒲂ׂ�
    for j in xrange(12):
        #print dow
        # ���̎n�߂����j�������ꍇcount��1���₷
        if dow == 0:
            count = count+1
            print j+1, "��"

        dow = (dow+(months[j]%7))%7

print "\n���v", count, "��"

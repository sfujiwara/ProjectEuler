# ��0-2���܂Œ�`
fibo_seq = [0, 1, 1]

i = 3
while(1):
    fibo_seq.append(fibo_seq[i-1]+fibo_seq[i-2])
    if len(str(fibo_seq[i])) >= 1000: break
    i = i+1

print i

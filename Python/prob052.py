def is_interesting(n):
    num_set = set([int(i) for i in str(n)])
    for i in xrange(2, 7):
        if not num_set == set([int(j) for j in str(i*n)]): return False
    return True

for i in xrange(1, 1000000):
    if is_interesting(i):
        print i
        break

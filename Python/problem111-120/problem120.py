print 'Answer:', sum(a*(a-2) if a%2 == 0 else a*(a-1) for a in range(3,1001))

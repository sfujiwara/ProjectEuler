# x‚ğy‚ÅŠ„‚èØ‚ê‚È‚­‚È‚é‚Ü‚ÅŠ„‚éŠÖ”
def remove_factor(x, y):
    if x%y == 0: return remove_factor(x/y, y)
    else: return x

def get_factors(n):
    factors = []
    i = 2
    while(True):
        if n%i == 0:
            factors.append(i)
            n = remove_factor(n, i)
        if n == 1: break
        i = i+1
    return factors

for i in xrange(100000, 1000000):
    if len(get_factors(i))==4:
        if len(get_factors(i+1))==4:
            if len(get_factors(i+2))==4:
                if len(get_factors(i+3))==4:
                    print i
                    break

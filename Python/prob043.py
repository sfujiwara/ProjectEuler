from itertools import permutations

# nŒ…‚Ìpandigital”‚ğƒŠƒXƒg‚Å•Ô‚·ŠÖ”
def get_pandigital_nums(n):
    p = []
    for i in permutations(range(n)):
        p.append(reduce(lambda x, y: x*10 + y, i))
    return p

def is_interesting(n):
    snum = str(n)
    if len(snum) != 10: return False
    if int(snum[1:4])%2 != 0: return False
    if int(snum[2:5])%3 != 0: return False
    if int(snum[3:6])%5 != 0: return False
    if int(snum[4:7])%7 != 0: return False
    if int(snum[5:8])%11 != 0: return False
    if int(snum[6:9])%13 != 0: return False
    if int(snum[7:10])%17 != 0: return False
    return True

ans = 0
for i in get_pandigital_nums(10):
    if is_interesting(i): ans = ans+i
    

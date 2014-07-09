n = 10000000
cache_list89 = [False]*n
cache_list1 = [False]*n

def converge_to_89(n):
    # 次の項を計算
    next_term = sum([int(i)**2 for i in str(n)])
    
    # 収束していれば判定結果を返す
    if next_term == 89: return True
    if next_term == 1: return False
    
    # キャッシュしたリストをチェックする
    if cache_list89[next_term]: return True
    if cache_list1[next_term]: return False
    
    # それ以外の場合は再帰
    return converge_to_89(next_term)

count = 0
for i in xrange(1,n):
    if converge_to_89(i):
        count += 1
        cache_list89[i] = True
    else: cache_list1[i] = True
    if i%100000==0: print i

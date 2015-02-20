# -*- coding: utf-8 -*-

'''
予め全ての約数の和を求めるところがちょっと重い.
時間は計ってないけれど, 3 分くらい掛かるかも.
'''

# Prime Factor Decomposition
# 出力は Ruby の prime_division と同じ
# x^a * y^b * z^c -> [[x, a], [y, b], [z, c]]
def pfd(n):
    prime_factors = []
    upper_threshold = n**0.5
    # 後のループを奇数だけで回すために, 2 だけ場合分けする
    if n % 2 == 0:
        factor = 2
        count = 0
        while n % factor == 0:
            n = n / factor
            count += 1
        prime_factors.append([factor, count])
    # 3 以上のの素因数を探す
    factor = 3
    while n > 1:
        # √n を超える素数は調べる必要がない
        if factor > upper_threshold:
            prime_factors.append([n, 1])
            break
        # 割り続けて素因数 factor を取り除く
        if n % factor == 0:
            count = 0
            while n % factor == 0:
                n = n / factor
                count += 1
            prime_factors.append([factor, count])
        # 3 以上の素数は全て奇数なので, 奇数だけ調べれば十分
        # 本当は素数だけを調べれば十分
        factor += 2
    return prime_factors

def sum_prop_devisors(n):
    res_pfd = pfd(n)
    res = 1
    for i in pfd(n):
        res *= (i[0]**(i[1]+1)-1) / (i[0]-1)
    return res - n


if __name__ == '__main__':
    N = 1000000
    ## 先に真の約数の和を全て求めておく
    sum_pd = [0,0] + [sum_prop_devisors(i) for i in range(2, N+1)]
    max_len_chain = 0
    for i in range(2, N+1):
        ## i を起点に友愛鎖を辿っていく
        path = [i]
        num = i
        while True:
            num = sum_pd[num]
            ## 1 に辿り着くか指定の範囲から逸脱した場合
            if num == 1 or num >= N:
                len_chain = -1
                break
            ## 一度通った場所を再度通った場合
            if num in path:
                ## 現在地を起点に再度友愛鎖を辿って長さを調べる
                init_num = num
                len_chain = 1
                members_cand = [num]
                while True:
                    num = sum_pd[num]
                    if num == init_num:
                        if len_chain > max_len_chain:
                            max_len_chain = len_chain
                            members = members_cand
                        break
                    len_chain += 1
                    members_cand.append(num)
                break
            path.append(num)

    print 'Answer:', min(members)

import math
import itertools

'''
外側を {6, 7, 8, 9, 10} で固定して 5-gon ring を列挙.
これで見つかれば, その中に解がある.
見つかってしまったので, 見つからなかった場合の処理は無し.
'''

if __name__ == '__main__':
    for i in itertools.permutations([1, 2, 3, 4, 5]):
        for j in itertools.permutations([6, 7, 8, 9, 10]):
            sol_set = [(j[0],i[0],i[1]), (j[1],i[1],i[2]),
                       (j[2],i[2],i[3]), (j[3],i[3],i[4]),
                       (j[4],i[4],i[0])]
            if len(set([sum(k) for k in sol_set])) == 1:
                if sol_set[0][0] == 6:
                    print 'Solution Set:', sol_set

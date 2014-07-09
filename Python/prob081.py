import csv

filename = "matrix.txt"
csvfile = open(filename)
mat = []

for row in csv.reader(csvfile):
    mat.append([int(i) for i in row ])

csvfile.close()

route = [[0] * 80 for i in range(80)]

for i in xrange(80):
    for j in xrange(80):
        if i==0 and j==0: pass
        elif i==0: mat[i][j] = mat[i][j-1] + mat[i][j]
        elif j==0: mat[i][j] = mat[i-1][j] + mat[i][j]
        else: mat[i][j] = min(mat[i-1][j], mat[i][j-1]) + mat[i][j]

print mat[-1][-1]

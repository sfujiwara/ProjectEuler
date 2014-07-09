import csv
import math

filename = "base_exp.txt"
csvfile = open(filename)
num_list = []

for row in csv.reader(csvfile):
    num_list.append([int(i) for i in row ])

csvfile.close()

index_max = 0
num_max = 0

for i in xrange(0, len(num_list)):
    tmp = num_list[i][1]*math.log10(num_list[i][0])
    print tmp
    if tmp > num_max:
        num_max = tmp
        index_max = i

"""
num_input = []
f = open("Problem18.txt")
test = f.read()
"""

num_list = []
for line in open('Problem18.txt'):
    itemList = line.split(' ')
    numbers = []
    for item in itemList:
        numbers.append( int(item) )
    num_list.append(numbers)

for i in xrange(len(num_list)-1, 0, -1):
    for j in xrange(len(num_list[i])-1):
        num_list[i-1][j] += max(num_list[i][j], num_list[i][j+1])


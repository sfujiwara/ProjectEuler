num = []

for i in xrange(2, 101):
    for j in xrange(2, 101):
        num.append(i**j)

num.sort()
num = list(set(num))
num.sort()

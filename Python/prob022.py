f = open("name.txt")
name = f.read()
name = name.replace('"', "")
name = name.split(",")
name.sort()

score = 0
for i in xrange(len(name)):
    tmp = 0
    for j in xrange(len(name[i])):
        tmp += ord(name[i][j])-64
    score += (i+1)*tmp



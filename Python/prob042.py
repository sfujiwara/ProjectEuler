# ÉtÉ@ÉCÉãÇÃì«Ç›çûÇ›
f = open("words.txt")
words = f.read()
words = words.replace('"', "")
words = words.split(",")

def triangle(n): return [i*(i+1)/2 for i in xrange(1, n+1)]

def get_score(word):
    score = 0
    for i in xrange(len(word)):
        score += ord(word[i])-64
    return score

t = triangle(100)
ans = 0
for i in xrange(len(words)):
    if get_score(words[i]) in t: ans += 1

print "Answer =", ans

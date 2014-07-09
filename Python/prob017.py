# ®”n‚ğ“ü‚ê‚é‚Æ’PŒê‚Ì’·‚³‚ğ•Ô‚·ŠÖ”
def get_length(n):
    spell1 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    spell2 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    spell10 = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 1<=n<=9:
        print spell1[n]
        return len(spell1[n])
    
    if 10<=n<=19:
        print spell2[n%10]
        return len(spell2[n%10])
    
    if 20<=n<=99:
        print spell10[n/10]+spell1[n%10]
        return len(spell10[n/10]+spell1[n%10])
    
    if n%100 == 0:
        print spell1[n/100]+"hundred"
        return len(spell1[n/100]+"hundred")

    if 110<=n<=119:
        print spell1[n/100]+"hundred"+"and"+spell2[n%10]
        return len(spell1[n/100]+"hundred"+"and"+spell2[n%10])
    
    if 100<=n<=999:
        print spell1[n/100]+"hundred"+"and"+spell10[(n%100)/10]+spell1[n%10]
        return len(spell1[n/100]+"hundred"+"and"+spell10[(n%100)/10]+spell1[n%10])


length_sum = 0
for i in xrange(1,1000):
    length_sum += get_length(i)

print length_sum + len("one"+"thousand")


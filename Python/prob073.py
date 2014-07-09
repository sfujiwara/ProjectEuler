count = 3
a, b = 3, 7
while True:
    if b+2 > 12000: break
    else:
        a, b = a+1, b+2
        count += 1
    
print a, b

def fact(x):
    if x<=1: return 1
    else: return x*fact(x-1)

2*fact(9) + 6*fact(8) + 6*fact(7) + 2*fact(6) + 5*fact(5) + 1*fact(4) + 2*fact(3) + 2*fact(2)

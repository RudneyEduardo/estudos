import math
linha1 = input().split(" ")
a, b, c = linha1
prima = (int(a) + int(b) + abs(int(a) - int(b))) / (2)
maior = (prima + int(c) + abs(prima - int(c)))/(2)
print("%d eh o maior" % maior)

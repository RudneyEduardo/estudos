import math
x = int(input())
tem_m = math.floor(x / 60) 
tem_h = math.floor(x / 3600)
secr = x - ((tem_m*60))
minr = tem_m - (tem_h*60)
print(repr(tem_h) + ":"+repr(minr) + ":" + repr(secr))


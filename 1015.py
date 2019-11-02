import math
p1 = input().split(" ")
p2 = input().split(" ")
x1, y1 = p1
x2, y2 = p2
a = math.pow(float(x2) - float(x1), 2)
b = math.pow(float(y2) - float(y1), 2)
resultado = math.sqrt(a + b)
print("%.4f"%resultado)

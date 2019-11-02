import math
linha1 = input().split(" ")
a, b, c = linha1
pi = 3.14159
tri = (float(a) * float(c)) / 2
cir =  pi * math.pow(float(c),2)
trap = ((float(a) + float(b)) * float(c)) / 2
quad = math.pow(float(b),2)
rect = float(a) * float(b)
print("TRIANGULO: {0:.3f}".format(tri))
print("CIRCULO: {0:.3f}".format(cir))
print("TRAPEZIO: {0:.3f}".format(trap))
print("QUADRADO: {0:.3f}".format(quad))
print("RETANGULO: {0:.3f}".format(rect))

a, b, c = input().split(" ")
if float(a) < float(b) + float(c) and float(b) < float(c) + float(a) and float(c) < float(b) + float(a):
    peri = float(a) + float(b) + float(c)
    print("Perimetro = {0:.1f}".format(peri))
else:
    area = ((float(a) + float(b))*float(c)) / 2
    print("Area = {0:.1f}".format(area))

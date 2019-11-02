x, y = input().split(" ")

if float(x) > 0 and float(y) > 0:
    print("Q1")
if float(x) > 0 and float(y) < 0:
    print("Q4")
if float(x) < 0 and float(y) > 0:
    print("Q2")
if float(x) < 0 and float(y) < 0:
    print("Q3")
if float(x) == 0 and float(y) != 0:
    print("Eixo Y")
if float(x) != 0 and float(y) == 0:
    print("Eixo X")
if float(x) == 0 and float(y) == 0:
    print("Origem")

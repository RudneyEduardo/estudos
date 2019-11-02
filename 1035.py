#entradas
a, b, c, d = input().split(" ")

#processamento e saída
e = int(c) + int(d) 
f = int(a) + int(b) 
g = int(a) % 2
if int(b) > int(c) and int(d) > int(a):
    if e > f and int(c) > 0:
        if int(d) > 0 and g == 0:
            print("Valores aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")
        

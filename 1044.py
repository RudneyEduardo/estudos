a, b = input().split()

res1 = int(b) % int(a)
res2 = int(a) % int(b)

if res1 == 0:
    print("Sao Multiplos")
elif res2 == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")

n = int(input())
i = 0
for i in range(0, n):
    pa, pb, g1, g2 = input().split(" ")
    pa = int(pa)
    pb = int(pb)
    g1 = float(g1)
    g2 = float(g2)
    anos = 0
    while int(pa) <= int(pb):
        contapa = int((pa*(g1/100)))
        contapb = int((pb*(g2/100)))
        anos += 1
        pa += contapa
        pb += contapb
        if anos > 100:
            break
    if (anos > 100):
        print("Mais de 1 seculo.")
    else:
        print("%d anos." %anos)

    
    

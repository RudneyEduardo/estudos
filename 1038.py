#programa mercado
a, b = input().split(" ")
res = int(b)

#processamento
if a == "1":
    res *= 4.0
    print("Total: R$ {0:.2f}".format(res))
elif a == "2":
    res *= 4.5
    print("Total: R$ {0:.2f}".format(res))
elif a == "3":
    res *= 5
    print("Total: R$ {0:.2f}".format(res))
elif a == "4":
    res *= 2
    print("Total: R$ {0:.2f}".format(res))
elif a == "5":
    res *= 1.5
    print("Total: R$ {0:.2f}".format(res))

nums = int(input('Digite aqui o número om 5 digitos!'))
notas = [100, 50, 20, 10, 2]
for x in notas:

    print(((nums/x) // 1), "Nota(s) de" , x)
    nums %= (x)

    



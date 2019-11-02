x = input().split()
n1, n2, n3, n4 = x
med = (float(n1)*2+ float(n2)*3 + float(n3)*4 + float(n4)*1) / 10
print("Média: {0:.1f}".format(med))
if med >= 7.0:
    print("Aluno aprovado.")
if med < 5.0:
    print("Aluno reprovado.")
if 5.0 <= med <= 6.9:
    print('Aluno em exame.')
    y = float(input())
    print('Nota do exame: {}'.format(y))
    m2 = (y + med) / 2
    if m2 >=5.0:
        print('Aluno aprovado.')
        print('Media final: {:.1f}'.format(m2))
    else:
        print('Aluno reprovado.')
        print('Media final: {:.1f}'.format(m2))

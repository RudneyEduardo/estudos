import math
tempo =  int(input())
anos = math.floor(tempo/365)
meses = math.floor((tempo % 365)/30)
dias = (tempo % 365) % 30
print('%d anos(s)'%anos)
print('%d mes(es)'%meses)
print('%d dia(s)'%dias)

n = int(input())

a = n // 365
n = n - a*365

m = n // 30
n = n - m*30

d = n

print('{} ano(s)'.format(a))
print('{} mes(es)'.format(m))
print('{} dia(s)'.format(d))

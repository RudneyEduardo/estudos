#1021

n = float(input())


m = n // 100
n = n % 100
o = n // 50
n = n % 50
p = n // 20
n = n % 20
q = n // 10
n = n % 10
r = n // 5
n = n % 5
s = n // 2
n = n % 2
t = n // 1
n = n % 1
u = n // 0.5
n = n % 0.5
v = n // 0.25
n = n % 0.25
w = n // 0.10
n = n % 0.10
x = n // 0.05
n = n % 0.05
y = n // 0.01
n = n % 0.01
print("NOTAS: ")
print("{0:.0f} nota(s) de R$ 100.00".format(m))
print("{0:.0f} nota(s) de R$ 50.00".format(o))
print("{0:.0f} nota(s) de R$ 20.00".format(p))
print("{0:.0f} nota(s) de R$ 10.00".format(q))
print("{0:.0f} nota(s) de R$ 5.00".format(r))
print("{0:.0f} nota(s) de R$ 2.00".format(s))
print("MOEDAS: ")
print("{0:.0f} moeda(s) de R$ 1.00".format(t))
print("{0:.0f} moeda(s) de R$ 0.50".format(u))
print("{0:.0f} moeda(s) de R$ 0.25".format(v))
print("{0:.0f} moeda(s) de R$ 0.10".format(w))
print("{0:.0f} moeda(s) de R$ 0.05".format(x))
print("{0:.0f} moeda(s) de R$ 0.01".format(y))


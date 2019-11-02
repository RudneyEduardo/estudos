hi, mi, hf, mf = input().split(" ")
hi = int(hi)
hf = int(hf)
mi = int(mi)
mf = int(mf)

hix = 3600*hi
hfx = 3600*hf
mfx = 60*mf
mix = 60*mi
res = (hfx+mfx)-(hix+mix)
resH = int(res/ 3600)
resM = int((res % 3600) / 60)
if res > 24:
    resH = 24
    resM = 0

if hi == mi and hf == mf and hi == hf and mi == mf and res == 0:
    if hi == 0 and hf == 0 and mi == 0 and mf == 0:
        resH = 0
        resM = 1
    else:
        resH = 24
        resM = 0

print("O JOGO DUROU {0} HORA(S) E {1} MINUTO(S)".format(resH, resM))



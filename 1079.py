n = int(input())
for i in range(1, n + 1):
    a, b, c = input().split(" ")
    media = (float(a)*0.2) + (float(b)*0.3) + (float(c)*0.5)
    print("{0:.1f}".format(media))

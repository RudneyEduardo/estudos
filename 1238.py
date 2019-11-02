n = int(input())
a3 = []
for i in range(1, n+1):
    str1, str2 = input().split()
    a1 = list(str1)
    a2 = list(str2)
    count = 0
    for w in range(0, len(a1)):
        res = a1[w] + a2[w]
        print(res)

n = int(input())
a = []
if 1 <= n <= 1000:
    while n > 0:
        j = 0
        w = n % 2
        if w != 0:
            print(n)
            n -= 1
       

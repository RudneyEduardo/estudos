n = int(input())
for i in range(1, n + 1):
    c = int(input())
    print(i)
    if c % i > 1:
        print("%d nao eh primo" %c)
    else:
        print("%d eh primo" %c)
    
        

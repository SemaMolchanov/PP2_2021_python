n = int(input())
k = int(input())
while True:
    if n == k:
        break
    if k <= n/2:
        if n % 2 == 1:
            print("-1")
            n -= 1
        if n % 2 == 0:
            print(":2")
            n /= 2
    else:
        print("-1")
        n -= 1
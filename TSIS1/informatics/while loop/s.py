n = int(input())
k = int(input())
while n > k:
    if (n >= k * 2):
        if n % 2 == 0:
            print(":2")
            n //= 2
        else:
            print("-1")
            n -= 1
    else:
        print("-1")
        n -= 1

num = int(input())
cnt = 0
while num != 0:
    num //= 10
    cnt += 1
print(cnt)

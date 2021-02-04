n = int(input())
cnt = 0
for i in range (n):
    i = int(input())
    if i == 0:
        cnt += 1
if cnt > 0:
    print('YES')
else:
    print('NO')
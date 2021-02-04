n = int(input())
num, cnt = 1, 1
s = ''
for i in range (n):
    if cnt == 0:
        num += 1
        cnt = num
    s += str(num) + ' '
    cnt -= 1
print(s)
    
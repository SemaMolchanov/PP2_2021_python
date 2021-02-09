n = int(input())
i = 1
s = ''
while i*i <= n:
    s += str(i*i) + ' '
    i += 1
print(s)
    
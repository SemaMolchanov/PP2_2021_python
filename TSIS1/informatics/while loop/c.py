n = int(input())
i = 0
s = ''
while 2**i <= n:
    s += str(2**i) + ' '
    i += 1
print(s)
    
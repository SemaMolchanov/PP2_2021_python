s = input()
c = ''
for i in range (len(s) - 1):
    tmp = s[i] + '*'
    c += tmp
print(c + s[len(s) - 1])


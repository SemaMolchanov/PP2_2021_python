s = input()
c = ''
for i in range (s.rindex('h'), s.index('h')):
    c += s[i]
print(s[:s.index('h')] + c + s[(s.rindex('h') + 1):])
s = input()
c = ''
for i in range (len(s)):
    if s[i] != '@':
        c += s[i]
print(c)
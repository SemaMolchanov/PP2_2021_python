s = input()
print(s[2])
print(len(s) - 2)
print(s[:5])
print(s[:len(s) - 1])
c, x, y = '', '', ''
for i in range (len(s)):
    if i % 2 == 0:
        c += s[i]
print(c)
for j in range (len(s)):
    if j % 2 != 0:
        x += s[j]
print(x)
for k in range (len(s), 1):
    y += s[k]
print(y)
print(len(s))
import re 
pattern = r'^[#]{1}[0-9A-Fa-f]{3,6}$'
t = int(input())
data = str()
for i in range (t):
    n = input()
    data = ' '.join(n)

matches = list(re.findall(pattern, data))
for j in matches:
    print(str(j))
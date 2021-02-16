lines = list()
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
    
txt = ' '.join(lines)
words = txt.split()
d = dict()
cnt, word = str(), str()
for i in words:
    cnt, word = words.count(i), i
    d[cnt] = word
print(d)

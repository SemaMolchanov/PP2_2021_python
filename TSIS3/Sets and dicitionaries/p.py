lines = list()
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
    
txt = ' '.join(lines)
words = txt.split()
pairs = set()
pair = tuple()
word, cnt = str(), str()
for i in words:
    pair = (words.count(i), i)
    pairs.add(pair)
sorted_pairs = sorted(pairs)
reversed_pairs = reversed(sorted_pairs)

for j in reversed_pairs:
    print(j[1])

    




from collections import Counter

lines = list()
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
    
txt = ' '.join(lines)
words = txt.split()

counter = Counter(sorted(words))
print(*sorted(counter.keys(), key=counter.get, reverse = True),sep='\n')


    




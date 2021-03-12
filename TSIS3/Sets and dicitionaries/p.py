#from collections import Counter

'''lines = list()
while True:
    line = input()
    if lines:
        lines.append(line)
    else:
        break'''

'''txt = ' '.join(lines)
words = txt.split()

counter = Counter(sorted(words))
print(*sorted(counter.keys(), key=counter.get, reverse = True),sep='\n')
'''

words = []

while True:
    line = input().split()
    if not line:
        break
    for word in line:
        words.append(word)

occurence = dict()

for word in words:
    if word in occurence:
        occurence[word] +=1
    else :
        occurence[word] = 1
    
occurence = sorted(([-value, key] for key, value in occurence.items()))

for key, value in occurence:
    print(value)


    




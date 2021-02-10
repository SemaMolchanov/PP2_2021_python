n = int(input())
d = dict()
for i in range (n):
    word, synonim = input().split()
    d[word] = synonim
search_word = input()
for word, synonim in d.items():
    if search_word == word:
        print(synonim)
    elif search_word == synonim:
        print(word)


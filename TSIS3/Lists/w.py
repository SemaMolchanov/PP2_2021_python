my_list = list(map(int, input().split()))
s1 = str()
s2 = str()
for i in my_list:
    if i == 0:
        s2 += str(i) + ' '
    else:
        s1 += str(i) + ' '
print(s1 + s2)
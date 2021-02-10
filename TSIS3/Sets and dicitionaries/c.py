my_set1 = set(map(int, input().split()))
my_set2 = set(map(int, input().split()))
my_set3 = my_set1.intersection(my_set2)
s = str()
for i in sorted(my_set3):
    s += str(i) + ' '
print(s)


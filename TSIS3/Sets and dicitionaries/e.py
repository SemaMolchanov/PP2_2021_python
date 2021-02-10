n, m = map(int, input().split())
anya = set()
borya = set()
for i in range (n):
    i = int(input())
    anya.add(i)
for j in range (m):
    j = int(input())
    borya.add(j)
common = anya.intersection(borya)
common_str = str()
for i in sorted(common):
    common_str += str(i) + ' '
anyas_only = anya.difference(borya)
boryas_only = borya.difference(anya)
anyas_only_str = str()
boryas_only_str = str()
for i in sorted(anyas_only):
    anyas_only_str += str(i) + ' '
for j in sorted(boryas_only):
    boryas_only_str += str(j) + ' '
print(len(common))
print(common_str)
print(len(anyas_only))
print(anyas_only_str)
print(len(boryas_only))
print(boryas_only_str)

    
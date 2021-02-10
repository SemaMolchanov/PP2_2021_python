def rotate (l, step):
    return l[-step:] + l[:-step]

my_list = list(map(int, input().split()))
k = int(input())
s = str()
new_list = rotate(my_list, k)
for i in new_list:
    s += str(i) + ' '
print(s)


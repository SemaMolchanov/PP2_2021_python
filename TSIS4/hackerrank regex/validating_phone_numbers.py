import re 
pattern = r'^[7-9]{1}[0-9]{9}$'
t = int(input())
my_list = list()
for i in range (t):
    n = input()
    my_list.append(n)

for string in my_list:
    if bool(re.match(pattern, string)):
        print('YES')
    else:
        print('NO')


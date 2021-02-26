import re 
pattern = r'^[-+]?[0-9]*\.[0-9]+$'
t = int(input())
my_list = list()
for i in range (t):
    n = input()
    my_list.append(n)

for string in my_list:
    print(bool(re.match(pattern, string)))
    


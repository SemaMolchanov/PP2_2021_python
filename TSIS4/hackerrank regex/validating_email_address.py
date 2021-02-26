import re
n = int(input())
for _ in range(n):
    username, email = input().split(' ')
    matches = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', email)
    if matches:
        print(username, email)
import sys
sys.setrecursionlimit(10**7)

n = int(input())
d = {}
all = set()
children = set()
for _ in range(n - 1):
    line = input().split()
    child = line[0]
    parent = line[1]
    all.add(parent)
    all.add(child)
    children.add(child)
    if d.get(parent, []) != []:
        d[parent].append(child)
    else:
        d[parent] = [child]
    
c = {}

def dfs(current):
    cur = 1
    for child in d.get(current, []):
        cur += dfs(child)
    c[current] = cur - 1
    return cur

main_ancestor = all.difference(children).pop()
dfs(main_ancestor)

for i in sorted(c.items()):
    print(i[0], i[1])
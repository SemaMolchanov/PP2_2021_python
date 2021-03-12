import re
n = re.search(r"([a-z0-9])\1+", input())
print(n.group(1) if n else -1)
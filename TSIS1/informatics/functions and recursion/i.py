from math import sqrt

def min_divisor(x, i = 2):
    if i > int(sqrt(x)) and x % i != 0:
        return x
    if x % i == 0:
        return i
    return min_divisor(x, i + 1)

n = int(input())
print(min_divisor(n))
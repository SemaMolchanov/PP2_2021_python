def gcd(a, b):
    if (a == 0 or b == 0):
        return a + b
    if a > b:
        return gcd(a % b, b)
    elif a < b:
        return gcd(a, b % a)

a = int(input())
b = int(input())
print(gcd(a, b))
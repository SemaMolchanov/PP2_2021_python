n = int(input())

divisors = [number for number in range(1, n) if n % number == 0]

print(n == sum(divisors))
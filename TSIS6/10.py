def is_even(n):
    if n % 2 != 0:
        return False
    return True

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(filter(is_even, my_list)))
import random

def random_line(file_name):
    '''lines = open(file_name).read().splitlines()
    return random.choice(lines)'''
    f = open(file_name)
    lines = f.readlines()
    return random.choice(lines)

print(random_line('test.txt'))
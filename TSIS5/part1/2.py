from itertools import islice

def read_first_lines(file_name, n):
    with open(file_name, 'r') as f:
        for line in islice(f, n):
            print(line)

n = int(input())
read_first_lines('test.txt', n)



















def read_first_lines(file_name, n):
    with open(file_name, 'r') as f:
        for i in range f.read().count('\n'):
            print(f.readline())
            

read_first_lines('test.txt', 2)



















def read_to_var(file_name):
    with open(file_name, 'r') as f:
        data = f.readlines()
        print(data)

read_to_var('test.txt')
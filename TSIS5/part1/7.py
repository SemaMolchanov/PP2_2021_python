def read_to_list(file_name):
    lines_arr = []
    with open(file_name, 'r') as f:
        for line in f:
            lines_arr.append(line)
        print(lines_arr)

read_to_list('test.txt')
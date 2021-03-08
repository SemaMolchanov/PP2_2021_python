lines_list = []
def read_to_list(file_name):
    with open(file_name, 'r') as f:
        global lines_list
        lines_list = f.readlines()
        print(lines_list)

read_to_list('test.txt')
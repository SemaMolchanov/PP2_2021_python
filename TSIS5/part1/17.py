def remove_newlines(file_name):
    f = open(file_name)
    file_list = f.readlines()
    return [line.rstrip('\n') for line in file_list]

print(remove_newlines("test.txt"))
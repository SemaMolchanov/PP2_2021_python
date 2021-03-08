def file_length(file_name):
    with open(file_name ,'r') as f:
        text = f.readlines()
        return len(text)

print('Number of lines in the file: ' + str(file_length('test.txt')))
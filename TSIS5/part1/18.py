def words_number(file_name):
    f = open(file_name)
    file_list = f.readlines()
    txt = ' '.join(file_list)
    words = txt.split()
    return len(words)

print(words_number("test.txt"))
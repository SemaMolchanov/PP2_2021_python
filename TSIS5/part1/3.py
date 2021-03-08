def append_and_display(file_name):
    with open(file_name, 'a') as f:
        data = input()
        f.write(data)
    txt = open(file_name)
    print(txt.read())


append_and_display('test.txt')
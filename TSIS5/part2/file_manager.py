import os, os.path, time, shutil

init_location = 'C:\\'
cur_location = init_location

def return_to_parent_dir():
    global cur_location
    if cur_location == init_location:
        print('no parent directory for disk C directory')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')
    else:
        parent_dir = os.path.abspath(os.path.join(cur_location, os.pardir))
        cur_location = parent_dir
        print('your current location is', cur_location)
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')

def change_directory():
    global cur_location
    print('enter the name of directory you want to move to')
    new_location = input()
    if os.path.exists(os.path.join(cur_location, new_location)):
        os.chdir(os.path.join(cur_location, new_location))
        cur_location = os.path.join(cur_location, new_location)
        print ('your current location is', cur_location)
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')
    else:
        print('this folder does not exist')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')

def rename_directory():
    global cur_location
    print('enter the name of the directory you want to rename')
    dir_name = input()
    if os.path.exists(os.path.join(cur_location, dir_name)):
        print('enter the new name')
        new_name = input()
        os.rename(os.path.join(cur_location, dir_name), os.path.join(cur_location, new_name))
        print('directory succesfuly renamed')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')
    else:
        print('such a directory does not exist')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')

def print_files_number():
    files_number = len([name for name in os.listdir(cur_location) if os.path.isfile(os.path.join(cur_location, name))])
    print('number of files in the current directory: ' + str(files_number))
    print('do you want to continue? (yes/no)')
    option = input()
    if option == 'yes':
        start()
    elif option == 'no':
        print('Thank you. Good bue')

def print_dirs_number():
    dirs_number = len([name for name in os.listdir(cur_location) if os.path.isdir(os.path.join(cur_location, name))])
    print('number of directories in the current directory: ' + str(dirs_number))
    print('do you want to continue? (yes/no)')
    option = input()
    if option == 'yes':
        start()
    elif option == 'no':
        print('Thank you. Good bue')
    pass

def list_content():
    print('all directories and files of the current directory')
    dir_list = os.listdir(cur_location)
    for directory in dir_list:
        print(directory)
    print('do you want to continue? (yes/no)')
    option = input()
    if option == 'yes':
        start()
    elif option == 'no':
        print('Thank you. Good bue')
    pass

def add_file():
    print('''
    enter the name of the file you want to create in the following format

                        file_name.extension''')
    default_data = str()
    global cur_location
    file_name = input()
    if not os.path.exists(os.path.join(cur_location, file_name)):
        with open(os.path.join(cur_location, file_name), 'a') as f:
            f.write(default_data)
            f.close()
        print('file created succesfully')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')
    else:
        ('such a file already exists')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')

def add_dir():
    print('enter the name of the directory you want to create')
    global cur_location
    dir_name = input()
    if not os.path.exists(os.path.join(cur_location, dir_name)):
        os.mkdir(os.path.join(cur_location, dir_name))
        print('''directory created succesfully''')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')
    else:
        print('such a directory already exists')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')

def delete_file():
    print('''enter name of the file you want to delete in the following format
    
                        file_name.extension''')
    file_name = input()
    if os.path.exists(os.path.join(cur_location, file_name)):
        os.remove(os.path.join(cur_location, file_name))
        print('file removed succesfully')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')
    else:
        print('such a file does not exist')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')

def rename_file():
    print('''enter name of the file you want to rename in the following format
    
                        file_name.extension''')
    file_name = input()
    if os.path.exists(os.path.join(cur_location, file_name)):
        print('''enter the new name in the following format
                        file_name.extension''')
        new_name = input()
        os.rename(os.path.join(cur_location, file_name), os.path.join(cur_location, new_name))
        print('file renamed succesfully')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')
    else:
        print('such a file does not exist')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')

def add_content():
    print('''enter name of the file you want to add content to in the following format
    
                        file_name.extension''')
    file_name = input()
    if os.path.exists(os.path.join(cur_location, file_name)):
        with open (os.path.join(cur_location, file_name), 'a') as f:
            print('enter data to write to the file')
            data = input()
            f.write(data)
            f.close
        print('content added succesfully')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')
    else:
        print('such a file does not exist')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')

def rewrite_content():
    print('''enter name of the file you want to add content to in the following format
    
                        file_name.extension''')
    file_name = input()
    if os.path.exists(os.path.join(cur_location, file_name)):
        with open (os.path.join(cur_location, file_name), 'w') as f:
            print('enter data to write to the file')
            data = input()
            f.write(data)
            f.close
        print('content added succesfully')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')
    else:
        print('such a file does not exist')
        print('do you want to continue? (yes/no)')
        option = input()
        if option == 'yes':
            start()
        elif option == 'no':
            print('Thank you. Good bue')
    pass

def options():
        print('''
        press a to rename the directory
        press b to print number of files in the directory
        press c to print number of directories in the directory
        press d to list content of the directory
        press e to add file to the directory
        press f to add new directory to the directory
        press g to change directory
        press h to delete file
        press i to rename file
        press j to add content to file
        press k to rewrite content of the file
        press l to return to the parent directory''')
        option = input()
        if option == 'a':
            rename_directory()
        elif option == 'b':
            print_files_number()
        elif option == 'c':
            print_dirs_number()
        elif option == 'd':
            list_content()
        elif option == 'e':
            add_file()
        elif option == 'f':
            add_dir()
        elif option == 'g':
            change_directory()
        elif option == 'h':
            delete_file()
        elif option == 'i':
            rename_file()
        elif option == 'j':
            add_content()
        elif option == 'k':
            rewrite_content()
        elif option == 'l':
            return_to_parent_dir()

def start():
    global cur_location
    print('you are now in the', cur_location, 'directory')
    options()

start()
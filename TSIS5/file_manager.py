import os, os.path, time, shutil

init_location = 'C:\\'
cur_location = init_location

def return_to_parent_dir():
    global cur_location
    if cur_location == init_location:
        print('No parent directory for disk C directory')
    else:
        cur_location = os.path.abspath(os.pardir)

def change_directory():
    global cur_location
    print('''
    press 1 to return to the parent directory
    press 2 to change directory''')
    option = int(input())
    if option == 1:
        return_to_parent_dir()
    elif option == 2:
        new_location = input()
        if os.path.exists(os.path.join(cur_location, new_location)):
            os.chdir(os.path.join(cur_location, new_location))
            cur_location = os.path.join(cur_location, new_location)
            print ('your current location is', cur_location)
        else:
            print('this folder does not exist')
    pass

def rename_directory():
    print('enter the name you want the directory to be changed to')
    old_name = cur_location
    new_name = input()
    os.rename(old_name, new_name)
    pass

def print_files_number():
    files_number = len([name for name in os.listdir(cur_location) if os.path.isfile(os.path.join(cur_location, name))])
    print(files_number)
    pass

def print_dirs_number():
    dirs_number = len([name for name in os.listdir(cur_location) if os.path.isdir(os.path.join(cur_location, name))])
    print(dirs_number)
    pass

def list_content():
    dir_list = os.listdir(cur_location)
    for directory in dir_list:
        print(directory)
    pass

def add_file():
    print('''
    Enter the name of the file you want to create in the following format

    file_name.extension''')
    default_data = str()
    global cur_location
    file_name = input()
    if not os.path.exists(os.path.join(cur_location, file_name)):
        with open(os.path.join(cur_location, file_name), 'a') as f:
            f.write(default_data)
            f.close()
    else:
        ('Such a file already exists')
    pass

def add_dir():
    print('Enter the name of the directory you want to create')
    global cur_location
    dir_name = input()
    if not os.path.exists(os.path.join(cur_location, dir_name)):
        os.mkdir(os.path.join(cur_location, dir_name))
    else:
        print('Such a directory already exists')
    pass

def delete_file():

    pass

def rename_file():
    pass

def add_content():
    pass

def rewrite_content():
    pass


def dir_options():
        print('''
        press 1 to rename the directory
        press 2 to print number of files in the directory
        press 3 to print number of directories in the directory
        press 4 to list content of the directory
        press 5 to add file to the directory
        press 6 to add new directory to the directory
        press 7 to change directory
        ''')
        option = int(input())
        if option == 1:
            rename_directory()
        elif option == 2:
            print_files_number()
        elif option == 3:
            print_dirs_number()
        elif option == 4:
            list_content()
        elif option == 5:
            add_file()
        elif option == 6:
            add_dir()
        elif option == 7:
            change_directory()

def file_options():
        print('''
        press 1 to delete file
        press 2 to rename file
        press 3 to add content to file
        prees 4 to rewrite content of the file
        press 5 to return to the parent directory''')
        option = int(input())
        if option == 1:
            delete_file()
        elif option == 2:
            rename_file()
        elif option == 3:
            add_content()
        elif option == 4:
            rewrite_content()
        elif option == 5:
            return_to_parent_dir()


def start():
    if os.path.isdir(cur_location):
        dir_options()
    elif os.path.isfile(cur_location):
        file_options()

start()
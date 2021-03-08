import os.path

def file_size(file_name):
        return os.path.getsize(os.path.join(os.getcwd(), file_name))

print("File size in bytes of a plain file: " + str(file_size("test.txt")))
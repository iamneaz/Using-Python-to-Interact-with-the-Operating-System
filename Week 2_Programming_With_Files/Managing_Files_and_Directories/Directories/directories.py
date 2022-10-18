import os
#   current directory python code is executing in use ---> getcwd
print(os.getcwd())
#   to make a directory ---> mkdir
# os.mkdir("new_dir")

#   to change directory ---> chdir
# os.chdir("new_dir")
# print(os.getcwd())

#   to remove directory ---> rmdir
# os.rmdir("new_dir")  # only works if the directory is empty

#   os.listdir function returns a list of all the files and sub-directories in a given directory.
directory = "website"
listOfDirectories = os.listdir(directory)
print(listOfDirectories)

for name in listOfDirectories:
    fullname = os.path.join(directory, name)
    if os.path.isdir(fullname):
        print("{} is a directory".format(fullname))
    else:
        print("{} is a file".format(fullname))

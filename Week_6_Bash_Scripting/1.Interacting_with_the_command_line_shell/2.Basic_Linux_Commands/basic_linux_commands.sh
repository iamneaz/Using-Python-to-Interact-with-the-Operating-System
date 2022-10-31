#   making new directory
mkdir new_directory
#   going to a directory
cd new_directory
#   getting out of a directory
cd ..
#   getting directory path
pwd
#   for copying files
cp ../spider.txt . # copying spider.txt from the previous folder (..) and pasting it to current folder (.)
#   contents of a directory
ls -l
#   to show hidden files
ls -la
#   to move a file
mv myfile.txt emptyfile.txt
#   to remove a file 
rm myfile.txt # deletes one file
rm * #  deletes all the file in the current directory
#   to remove a directory
rmdir directory/ #  it would not work if any file is in it
#   getting input from a file
./streams_err.py < newfile.txt
#   and catching the error while doing it in a new file
#   here 2 represents the file descriptor STDERR , 0 represents STDIN, 1 represents STDOUT 
./streams_err.py < newfile.txt 2> error_file.txt

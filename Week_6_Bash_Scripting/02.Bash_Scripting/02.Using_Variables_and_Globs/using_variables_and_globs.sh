example=hello #no space between 
echo $example
# globs --> characters that allow us to create list of files
# most common globs are * and ?
echo *.py # will show all the files which end with .py in the directiory
echo c* # will show all the files that have the character c as the prefix
echo * # will show all the files in that directory
# use ? for only one character 
echo ?????.py # will show the python file with 5 characters
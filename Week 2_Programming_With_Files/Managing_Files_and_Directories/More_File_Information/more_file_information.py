import datetime
import os
#   get size of a file
filesize = os.path.getsize("dummyFile.txt")
print("The file size is {}".format(filesize))

#   check when the file was last modified
lastModified = os.path.getmtime("dummyFile.txt")  # returns a unix timestamp
print("File was last modified on {}".format(lastModified))

#   datetime for date and time
timestamp = os.path.getmtime("dummyFile.txt")
fileDateTime = datetime.datetime.fromtimestamp(timestamp).date()
print("File creation datetime : {}".format(fileDateTime))

#   absolute path
fileAbsolutePath = os.path.abspath("dummyFile.txt")
print("File Absolute Path : {}".format(fileAbsolutePath))

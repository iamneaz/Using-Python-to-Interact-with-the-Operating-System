import os
# deleting a file
os.remove("novel.txt")
# renaming a file
os.rename("first_draft.txt", "finished_masterpiece.txt")
# if file exists
os.path.exists("finished_masterpiece.txt")

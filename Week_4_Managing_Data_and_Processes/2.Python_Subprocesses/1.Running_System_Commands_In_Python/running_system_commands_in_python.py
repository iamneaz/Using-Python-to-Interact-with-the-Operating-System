import subprocess

# print(subprocess.run(["date"]))

# subprocess.run(["sleep", "2"])

result = subprocess.run(["ls", "this_File_Does_Not_exist"])
print(result.returncode)

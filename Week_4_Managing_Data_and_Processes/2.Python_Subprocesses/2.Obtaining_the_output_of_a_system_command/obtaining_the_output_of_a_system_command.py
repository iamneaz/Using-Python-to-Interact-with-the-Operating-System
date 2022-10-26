import subprocess

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.returncode)

print(result.stdout)
# the output comes in byte string

print(result.stdout.decode().split())

result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print("Now lets check the contents of STDOUT and STDERR attributes")
print("STDOUT")
print(result.stdout)
print("STDERR")
print(result.stderr)

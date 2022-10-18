filepath = r"D:\Using Pyrhon to Interact with the Operating System\spyder.txt"
with open(filepath) as file:
    for line in file:
        # print(line.upper())
        print(line.strip().upper())

file = open(filepath)
lines = file.readlines()
file.close()
lines.sort()
print(lines)

import csv
file = open("csv_file.txt")
csv_file = csv.reader(file)

for row in csv_file:
    name, phone, role = row
    print("Name : {}, Phone : {}, Role : {}".format(name, phone, role))

file.close()

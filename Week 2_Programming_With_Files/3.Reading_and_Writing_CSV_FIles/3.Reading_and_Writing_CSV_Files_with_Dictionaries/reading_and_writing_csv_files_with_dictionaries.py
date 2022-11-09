import csv
with open("software.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has {} users".format(row["name"], row["users"]))
#   we want to write bellow dictionary to a file
users = [
    {"name": "Sol Mansi",
     "username": "solm",
     "department": "iT Infrastructure"
     },
    {"name": "Lio Nelson",
     "username": "lion",
     "department": "User Experience Research"
     },
    {"name": "Charlie Grey",
     "username": "greyc",
     "department": "Development"
     }
]

#   first we define a list of keys
keys = ["name", "username", "department"]

with open("by_department.csv", "w") as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

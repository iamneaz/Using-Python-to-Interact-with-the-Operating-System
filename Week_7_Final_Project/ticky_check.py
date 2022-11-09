import re
import csv
import operator

error = {}
per_user = {}
filepath = "syslog.log"
error_list = []
per_user_list = []


def populateErrorDictionary(errorMessage):
    if errorMessage in error.keys():
        error[errorMessage] += 1
    else:
        error[errorMessage] = 1


def addNewItemToPerUserDictionary(userName):
    per_user[userName] = {}
    per_user[userName]["INFO"] = 0
    per_user[userName]["ERROR"] = 0


def updateItemInPerUserDictionary(userName, code):
    if code == "INFO":
        per_user[userName]["INFO"] += 1
    elif code == "ERROR":
        per_user[userName]["ERROR"] += 1


with open(filepath) as file:
    for line in file:
        result = re.search(
            r"ticky: ([\w+]*):? ([\w' ]*) [\[[#0-9]*\]?]? ?\((.*)\)$", line)
        code, errorMessage, userName = result.group(
            1), result.group(2), result.group(3)
        populateErrorDictionary(errorMessage)
        if userName in per_user:
            updateItemInPerUserDictionary(userName, code)
        else:
            addNewItemToPerUserDictionary(userName)
            updateItemInPerUserDictionary(userName, code)

error_list = sorted(error.items(), key=operator.itemgetter(1), reverse=True)

for key in per_user:
    per_user_list.append(
        (key, per_user[key]["INFO"], per_user[key]["ERROR"]))
per_user_list.sort(key=operator.itemgetter(0))

error_list.insert(0, ("Error", "Count"))

per_user_list.insert(0, ("Username", "INFO", "ERROR"))

with open("error_message.csv", "w") as error_message:
    writer = csv.writer(error_message)
    writer.writerows(error_list)

with open("user_statistics.csv", "w") as user_statistics:
    writer = csv.writer(user_statistics)
    writer.writerows(per_user_list)

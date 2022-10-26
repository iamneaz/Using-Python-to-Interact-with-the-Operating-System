from http.client import CONTINUE
import sys
import re

logfile = sys.argv[1]
usernames = {}

pattern = r"USER \((\w+)\)$"
with open(logfile) as f:
    for line in f:
        if "CRON" in line:
            result = re.search(pattern, line)
            if result is None:
                continue
            name = result[1]
            usernames[name] = usernames.get(name, 0) + 1
print(usernames)

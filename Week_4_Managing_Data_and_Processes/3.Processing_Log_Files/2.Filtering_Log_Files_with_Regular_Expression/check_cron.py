from http.client import CONTINUE
import sys
import re

logfile = sys.argv[1]
pattern = r"USER \((\w+)\)$"
with open(logfile) as f:
    for line in f:
        if "CRON" in line:
            result = re.search(pattern, line)
            print(result[1])

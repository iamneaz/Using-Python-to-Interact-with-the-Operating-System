import re

line = "Jan 31 00:09:39 ubuntu.local ticky: INFO Created ticket [#4217] (mdouglas)"
# To match a string stored in line variable, we use the search() method by defining a pattern.
re.search(r"ticky: INFO: ([\w] )*", line)
# You can also get the ERROR message as we did for the INFO log above from the ERROR log line.
line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
# To match a string stored in a line variable, we use the search() method by defining a pattern.
re.search(r"ticky: ERROR: ([\w ]*) ", line)

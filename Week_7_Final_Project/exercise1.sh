# To grep all the logs from ticky, use the following command:
grep "ticky" syslog.log
# In order to search all the ERROR logs, use the following command:
grep "ERROR" syslog.log
# To enlist all the ERROR messages of specific kind use the below syntax.
# Syntax: grep ERROR [message] [file-name]
grep "ERROR Tried to add information to closed ticket" syslog.log
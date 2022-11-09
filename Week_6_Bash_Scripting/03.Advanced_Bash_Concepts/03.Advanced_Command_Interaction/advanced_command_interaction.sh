tail /var/log/syslog | cut -d' ' -f5- 
#  we're passing dash d space to cut to tell it that we want to use a space as a delimiter, and dash f5 dash that tell it that we want to print the field number 5 and everything that comes after it

cut -d' ' -f5- /var/log/syslog | sort | uniq -c | sort -nr | head
# CTRL+Z send SIGSTOP
# fg command runs the previous command once more
# to stop a program stop cleanly ---> CTRL+C
# to terminate a command -- kill command -- sends SIGTERM
# kill command needs to run on a seperate terminal and we also need to know the process ID or PID of the program to kill
# command ps gives the pid
# command ps ax gives the pid of all the running processes
ps ax | grep ping  
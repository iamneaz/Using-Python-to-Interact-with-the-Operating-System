import os
import subprocess

#  Calling the copy method of the OS environ dictionary that contains the current environment variables.
# This creates a new dictionary that we can change as needed without modifying the original environment.
my_env = os.environ.copy()
#   Adding one extra directory to the path variable.
#   Remember, the path variable indicates where the operating system will look for the executable programs. By adding one entry to the path, we're telling the OS to look for programs in an additional location.
#   To create the new value, we're calling the join method on the OS path substring. This joins elements of the list that we're passing with a path separator corresponding to the current operating system.
#   So here, we're joining /opt/myapp and the old value of the path variable to the path separator

my_env["PATH"] = os.pathsep.join(["/opt/myapp", my_env["PATH"]])

#   Finally, we call the myapp command, setting the end parameter to the new environment that we've just prepared.
result = subprocess.run(["myapp"], env=my_env)

#   If we're automating a one-off, well-defined task, we're developing a solution quickly is the biggest requirement, then using system commands and subprocesses can help a lot. But if we're doing something more complex or long-running, it's usually a good idea to use the baked-in or external modules that Python provides.

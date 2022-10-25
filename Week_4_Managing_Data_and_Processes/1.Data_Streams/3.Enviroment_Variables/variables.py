import os

# The getMethod is a bit similar to how we've been accessing dictionary values up until now. The difference is what happens when the value isn't present. When we retrieve a value from a dictionary using the key as in OS.environ[fruit] and the key isn't present, we get an error. If we use a getMethod instead, we can specify what value should be returned if the key isn't present. In other words, the getMethod allows us to specify a default value when the key that we're looking for isn't in the dictionary. So what we're asking Python to do is try to retrieve the value associated with the key, but if the key's not defined return an empty string instead.

print("HOME: " + os.environ.get("HOME",""))
print("SHELL: " + os.environ.get("SHELL",""))
print("FRUIT: " + os.environ.get("FRUIT",""))

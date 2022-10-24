import re

# Capturing groups are portions of the pattern that are enclosed in parentheses.
# Let's say that we have a list of people's full names. These names are stored as last name, comma, first name. We want to turn this around and create a string that starts with the first name followed by the last name. We can do this using a regular expression with capturing groups.
# Let's see how this works. First we'll create a matching pattern that matches a group of letters followed by a comma, a space, and then another group of letters. To capture our groups, we'll put each group of letters between parentheses like this.

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)

# Because we defined two separate groups, the group method returns a tuple of two elements.
print(result.groups())

# We can also use indexing to access these groups. The first element contains the text matched by the entire regular expression. Each successive element contains the data that was matched by every subsequent match group. So let's look at the element at index 0.

print(result[0])

# That's the whole string. Now, the following index is correspond to each of the captured groups.

print(result[1])

# So we can construct the name that we want by using these indexes.

print("{} {}".format(result[2], result[1]))


def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])


print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))

# Fix the regular expression used in the rearrange_name function so that it can match middle names, middle initials, as well as double surnames.

#"^([\w \.-]*), ([\w \.-]*)$"


def rearrange_name(name):
    result = re.search(r"^(\w*), (\w* \w\.)$", name)
    if result == None:
        return name
    return "{} {}".format(result[2], result[1])


name = rearrange_name("Kennedy, John F.")
print(name)

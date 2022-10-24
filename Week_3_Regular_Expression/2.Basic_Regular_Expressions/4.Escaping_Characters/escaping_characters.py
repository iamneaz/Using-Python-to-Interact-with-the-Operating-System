import re

# . * + ? ^ $ []

print(re.search(r".com", "welcome"))

# To match an actual dot, we need to use an Escape character, which in the case of regular expressions is a backslash character.

print(re.search(r"\.com", "welcome"))

print(re.search(r"\.com", "neazahmedneaz@gmail.com"))

#  When we see a pattern that includes a backslash, it could be escaping a special regex character or a special string character. Using raw strings, like we've been doing, helps avoid some of these possible confusion because the special characters won't be interpreted when generating the string. They will only be interpreted when parsing the regular expression. On top of this, Python also uses the backslash for a few special sequences that we can use to represent predefined sets of characters. For example, \w matches any alphanumeric character including letters, numbers, and underscores.

print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "And_this_is_another"))

# \d for matching digits,
# \s for matching whitespace characters like space, tab or new line,
# \b for word boundaries
# and a few others.

# Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters (including letters, numbers, and underscores) separated by one or more whitespace characters.


def check_character_groups(text):
    result = re.search(r"\w .*\w", text)
    return result != None


print(check_character_groups("One"))  # False
print(check_character_groups("123  Ready Set GO"))  # True
print(check_character_groups("username user_01"))  # True
print(check_character_groups("shopping_list: milk, bread, eggs."))  # False

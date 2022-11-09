import re

print(re.search(r"A.*a", "Argentina"))

print(re.search(r"^A.*a$", "Azerbaijan"))

pattern = r"^[a-zA-z_][a-zA-z0-9_]*$"

print(re.search(pattern, "_this_is_a_valid_variable"))

print(re.search(pattern, "this isn't a valid variable name"))

print(re.search(pattern, "my_variable1"))

# Fill in the code to check if the text passed looks like a standard sentence, meaning that it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point.


def check_sentence(text):
    result = re.search(r"^[A-Z][a-z ].*[\.\?\!]$", text)
    return result != None


print(check_sentence("Is this is a sentence?"))  # True
print(check_sentence("is this is a sentence?"))  # False
print(check_sentence("Hello"))  # False
print(check_sentence("1-2-3-GO!"))  # False
print(check_sentence("A star is born."))  # True

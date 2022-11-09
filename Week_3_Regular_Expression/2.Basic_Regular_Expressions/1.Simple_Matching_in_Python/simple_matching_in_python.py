import re

# ALWAYS USE RAW STRINGS FOR REGULAR EXPRESSION IN PYTHON

result = re.search(r"aza", "plaza")
print(result)
result = re.search(r"aza", "bazaar")
print(result)
result = re.search(r"aza", "dona")
print(result)
print(re.search("^x", "xenon"))
print(re.search("p.ng", "penguin"))

# Fill in the code to check if the text passed contains the vowels a, e and i, with exactly one occurrence of any other character in between.


def check_aei(text):
    result = re.search(r"a.e.i", text)
    return result != None


print(check_aei("academia"))  # True
print(check_aei("aerial"))  # False
print(check_aei("paramedic"))  # True

# For Case insensitive
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))

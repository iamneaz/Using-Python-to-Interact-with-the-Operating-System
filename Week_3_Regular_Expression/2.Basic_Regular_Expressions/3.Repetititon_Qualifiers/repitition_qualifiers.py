import re

# we're going check out how to match these characters several times. So we wanted to find the longest word in the string, or we wanted to find the host names in a log file by checking for a bunch of alphanumeric characters between brackets. We can do this using another interesting RegEx concept, repeated matches. It's quite common to see expressions that include a dot followed by a star. This means that it matches any character repeated as many times as possible including zero

print(re.search(r"Py.*n", "Pygmalion"))

print(re.search(r"Py.*n", "Python Programming"))

print(re.search(r"Py[a-z]*n", "Python Programming"))

# . Other implementations like the one used by Python or by the Egrep command include two additional repetition qualifiers plus and question mark, that can help us construct more complex expressions. Let's check that out. The plus character matches one or more occurrences of the character that comes before it. So we had the pattern O plus L plus.

print(re.search(r"o+l+", "goldfish"))

print(re.search(r"o+l+", "woolly"))

# The repeating_letter_a function checks if the text passed includes the letter "a" (lowercase or uppercase) at least twice. For example, repeating_letter_a("banana") is True, while repeating_letter_a("pineapple") is False. Fill in the code to make this work.


def repeating_letter_a(text):
    result = re.search(r"[aA].*a", text)
    return result != None


print(repeating_letter_a("banana"))  # True
print(repeating_letter_a("pineapple"))  # False
print(repeating_letter_a("Animal Kingdom"))  # True
print(repeating_letter_a("A is for apple"))  # True

# The question mark symbol is yet another multiplier. It means either zero or one occurrence of the character before it.

print(re.search(r"p?each", "to each their own"))

print(re.search(r"p?each", "I like peaches"))

import re
# What if we wanted a pattern that repeats a specific number of times? This could happen if we're processing a line that we know has some specific data in a column, or we know that we want a string of a specific length. In cases like those, we would manually write the same pattern as many times as we need it. But it would be hard to read and hard to maintain. And that's why Python also offers numeric repetition qualifiers. These are written between curly brackets and can be one or two numbers specifying a range

print(re.search(r"[a-zA-z]{5}", "a ghost"))

#   What if we wanted to match all the words that are exactly five letters long?
#   We can do that using \b, which matches word limits at the beginning and end of the pattern, to indicate that we want full words

print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))

#    if we wanted to match a range of five to ten letters or numbers, we could use an expression like this one.

print(re.findall(r"\w{5,10}", "I really like strawberries"))

#   A number followed by a comma means at least that many repetitions with no upper boundary limited only by the maximum repetitions in the source text.

print(re.findall(r"\w{5,}", "I really like strawberries"))

#   a comma followed by a number means from zero up to that amount of repetitions
print(re.findall(r"s\w{,20}", "I really like strawberries"))

#   exactly given number

print(re.findall(r"\w{5}", "I really like strawberries"))

# The long_words function returns all words that are at least 7 characters. Fill in the regular expression to complete this function.


def long_words(text):
    pattern = r"\w{7,}"
    result = re.findall(pattern, text)
    return result


print(long_words("I like to drink coffee in the morning."))  # ['morning']
# ['chocolate', 'afternoon']
print(long_words("I also have a taste for hot chocolate in the afternoon."))
print(long_words("I never drink tea late at night."))  # []

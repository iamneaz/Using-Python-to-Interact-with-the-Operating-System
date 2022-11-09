import re

print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[a-z]way", "Stairway to heaven"))

print(re.search("cloud[a-zA-Z0-9]", "cloudy"))

# Fill in the code to check if the text passed contains punctuation symbols: commas, periods, colons, semicolons, question marks, and exclamation points.


def check_punctuation(text):
    result = re.search(r"[,.:;?!]", text)
    return result != None


print(check_punctuation("This is a sentence that ends with a period."))  # True
print(check_punctuation("This is a sentence fragment without a period"))  # False
print(check_punctuation("Aren't regular expressions awesome?"))  # True
print(check_punctuation("Wow! We're really picking up some steam now!"))  # True
print(check_punctuation("End of the line"))  # False

# Characters aren't in a group , To do that, we use a circumflex inside the square brackets. [^]

print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "i like cats and dogs"))

# If we want to get all possible matches, we can do that using the findall function
print(re.findall(r"cat|dog", "i like cats and dogs"))

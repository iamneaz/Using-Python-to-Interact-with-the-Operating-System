import re

print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))

#   If we want our split list to include the elements that we're using to split the values we can use capturing parentheses

print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))

#    Another interesting function provided by the RE module is called sub. It's used for creating new strings by substituting all or part of them for a different string, similar to the replace string method but using regular expressions for both the matching and the replacing. Let's see this in an example. So we had some logs in our system that included e-mail addresses of users and we wanted to anonymize the data by removing all the addresses. We could do that by using an expression.

print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]",
             "Received an email for go_nuts95@my.example.com")
      )

#   Let's now look at an example using sub where we use regular expressions for the replacing. For that, we'll go back to our code that switched the order of names of people and use sub to create the new string.

print(
    re.sub(
        r"^([\w .-]*), ([\w .-]*)$",
        r"\2 \1",
        "Lovelace, Ada"
    )
)

#   In the first parameter, we've got an expression that contains the two groups that we want to match: one before the comma and one after the comma. We want to use a second parameter to replace the matching string. We use backslash two to indicate the second captured group followed by a space and backslash one to indicate the first captured group. When referring to captured groups, a backslash followed by a number indicates the corresponding captured group. This is a general notation for regular expressions, and it's used by many tools that support regexes, not just Python. We can also use them to match patterns that repeat themselves which use capturing groups as back references.

#   QUESTION
#   We want to split a piece of text by either the word "a" or "the", as implemented in the following code. What is the resulting split list?
print(re.split(r"the|a", "One sentence. Another one? And the last one!"))

import operator
# create a dictionary.
fruit = {"oranges": 3, "apples": 5, "bananas": 7,
         "pears": 2}
# Call the sorted function to sort the items in the dictionary.
sorted(fruit.items())

# Pass the function itemgetter() as an argument to the sorted() function. Since the second element of tuple needs to be sorted, pass the argument 0 to the itemgetter function of the operator module.
sorted(fruit.items(), key=operator.itemgetter(0))

# To sort a dictionary based on its values, pass the argument 1 to the itemgetter function of the operator module.
sorted(fruit.items(), key=operator.itemgetter(1))

# To sort the fruit object from most to least occurrence, we pass the argument reverse=True.
sorted(fruit.items(), key=operator.itemgetter(1), reverse=True)

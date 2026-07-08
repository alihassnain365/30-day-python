age = [22, 19, 24, 25, 26, 24, 25, 24]
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(age_set)
# Explain the difference between the following data types: string, list, tuple and set
    # string used to store the text 
    # list are modifiable, mutable arrays in python ordered
    # tupples are unmutable , unmodifiable , ordered data type
    # set are unordered
# I am a teacher and I love to inspire and teach people. How many unique words have been used
print(len('I am a teacher and I love to inspire and teach people'))
# in the sentence? Use the split methods and set to get the unique words.
word = set(("I am a teacher and I love to inspire and teach people").split())
print(word)
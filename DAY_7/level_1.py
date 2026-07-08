# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies

print(len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
# Insert multiple IT companies at once to the set it_companies
it_companies.update(['X', 'DevSinc'])
# Remove one of the companies from the set it_companies
it_companies.remove('X')
# What is the difference between remove and discard
# remove try to delete and if doenst exist it throws an error, while discard dont throw an error


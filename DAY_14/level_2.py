countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']


countries_list = list(map(lambda country : country.upper(),countries))

print(countries_list)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# now creating the square of the numbers using map function

numbers_square = list(map(lambda number : number*number, numbers))
print(numbers_square)

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
# now using map function  to create the upper case list

names_upper = list(map(lambda name: name.upper(), names))
print(names_upper)



# Use filter to filter out countries containing 'land'. 


land_countries = list(filter(lambda country : country[-4:]=='land',countries))
print(land_countries)


# Use filter to filter out countries having exactly six characters.

six_character_countries = list(filter(lambda country: len(country) == 6, countries))
print(six_character_countries)
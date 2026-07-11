numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

# now filtering the non-negative numbers
numbers = [i for i in numbers if i >= 0]
print(numbers)


# now flattering the 2d array to 1d

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

list_of_lists = [number for row in list_of_lists for number in row]

print(list_of_lists)


countries = [('Finland', 'Helsinki'), ('Sweden', 'Stockholm'), ('Norway', 'Oslo')]

# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

result = [
            [country.upper(),country[:3].upper(), capital.upper()]
            for (country, capital) in countries
        ]

print(result)


names = [[('Ali', 'Hassnain')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Ali Hassnain', 'David Smith', 'Donald Trump', 'Bill Gates']

full_names = [
                first_name + ' ' + last_name
                for[(first_name,last_name)] in names
            ]

print(full_names)


# Write a lambda function which can solve a slope or y-intercept of linear functions.

slope = lambda x1,y1,x2,y2 : (y2-y1)/(x2-x1) (2,3,6,11)

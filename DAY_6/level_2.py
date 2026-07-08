sisters = ('M Ulfat', 'F Ulfat', 'T Abid') # just crying - I would sacrifice myself for happiness of this tupple
brothers = ('Sunny', 'Shehri','Shami')

siblings = (*sisters,*brothers)
print(siblings)


family_members = (*siblings, 'Ulfat Hussain', 'A Mafi', 'K BB')
print(family_members)

*siblings1,father,mother1,mother2 = family_members
print(siblings1)
print(father)
print(mother1)
print(mother2)


# Create fruits, vegetables and animal products tuples.
#  Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('apple', 'banana', 'mango')
vegetables = ('tomato', 'potato', 'onion')
animal = ('peacock', 'horse', 'lion')

food_stuff_tp = (*fruits, *vegetables, *animal)
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# now finding middle from the tupple

print(food_stuff_tp[len(food_stuff_tp)//2])

# deleting the fodd stuff tupple
del food_stuff_tp


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
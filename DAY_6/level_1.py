# tuple are unchangeable unmodifiable
# mean we could create them once, not insert anything in them , 
# not could delte a single item from them
# tuples are ordered
# allow duplicates



# creating a tuple

tuple1 = tuple()
tuple2 = tuple(('ali', 1, 'shami', 2))
tuple3 = (1,2,3,'sunny', 'i love you')

sisters = ('M Ulfat', 'F Ulfat', 'T Abid') # just crying - I would sacrifice myself for happiness of this tupple
brothers = ('Sunny', 'Shehri','Shami')

siblings = (*sisters,*brothers)
print(siblings)

# now counting how many siblings i have
print(len(siblings))

family_members = (*siblings, 'Ulfat Hussain', 'A Mafi', 'K BB')
print(family_members)

# creating list
it_companies = list()
it_companies = ['Facebook', 'Google', 'IBM', 'Amazon', 'Netflix', 'Oracle']
print(f"Companies are {it_companies}")
print(f"Number of items in the list are : {len(it_companies)}")

# modifying
it_companies[4] = 'Systems'
print(f"Modified list {it_companies}")

# adding new item
it_companies.append('DevSince') # add the item at the end
print(it_companies)
it_companies.extend(['Programming Force','Hubble']) # add the multiple items at the end
print(it_companies)
it_companies.insert(2,'Invisible Technologies') # add the element at the entered syntax
print(it_companies)

# inserting the company in the middle - using insert
it_companies.insert(len(it_companies)//2, 'UCP')
print(it_companies)

# now uppercasing a list item
it_companies[4] = it_companies[4].upper()
print(it_companies[4])

l2 = ['ali','shehri','shami']
# now joining
it_companies = it_companies + list('#') + l2
print(f"Joined list is  : {it_companies}")


# now checking if the certain company exists in the list
print('UCP' in it_companies)
print('ali' in it_companies)
print('arshman' in it_companies)

# now sorting the list - python sort function uses timsort sorting that results in O(nlogn) time complexit and O(n) space complexit

it_companies.sort() # sort() function changes the original list
print(it_companies)
it_companies.sort(reverse=True) # this syntax sorts the list in desc

it_companies.reverse()
print(f"Reversed list is {it_companies}")

# now slicing the some elements

print(f"Here are the first three sliced companies : {it_companies[:3]}")

print(f"Here are the last three sliced items : {it_companies[-3:]}")

it_companies.append('scribble')

if(len(it_companies) % 2 == 1):
    print(f"Middle is  : {it_companies[len(it_companies)//2]}")
else:
    print(f"Middle element are  : {it_companies[len(it_companies)//2: len(it_companies)//2 + 2]}")

print('Oracle' in it_companies)
# removing the middle item from the list - using pop(inded) - pop() removes the last element
# pop returns the delted item
print("Element removed is : ",it_companies.pop(len(it_companies)//2))

print('Oracle' in it_companies)

# deleting the first element - using del
del it_companies[0] 
print(it_companies)

#it_companies.insert(len(it_companies)//2,'Eleven')
print(it_companies)

print(it_companies[len(it_companies)//2])
# now removing the middle element or elements
if (len(it_companies) % 2 == 1):
    del it_companies[len(it_companies)//2]
else:
    del it_companies[len(it_companies)//2: len(it_companies)//2 + 2]
print(it_companies)


# now removing all the items - using clear() - del list_name[:]
it_companies.clear()
print(it_companies)

# now destroying the list - it completely deltes the variable object
del it_companies

print(it_companies) # this would throw an error as there is no it_companies as it was destroyed


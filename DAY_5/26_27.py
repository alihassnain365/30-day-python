front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

# now joining these two lists
front_end = [*front_end , *back_end]
# you can use any other like l1 + l2 , but this method also works for different data types
# like list + tupple would give error , but not in this method [*list, *tupple]
print(front_end)

# now copying

# we cant use a=b , in this the both are pointing to the same list , one could change other
# insted we use these methods
# b = a.copy()  ---- b = a[:] 
full_stack = front_end.copy()
print(full_stack)